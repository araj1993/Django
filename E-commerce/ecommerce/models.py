from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinValueValidator
from decimal import Decimal


class UserManager(BaseUserManager):
    """Custom user manager for the simplified User model."""
    
    def create_user(self, username, email, password=None):
        """Create a regular user."""
        if not username:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None):
        """Create a superuser."""
        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Simplified User model for the e-commerce platform.
    Contains only: id, username, password, email
    """
    # Primary key (id) is automatically created by Django
    username = models.CharField(
        max_length=150, 
        unique=True, 
        help_text="Unique username"
    )
    password = models.CharField(
        max_length=128, 
        help_text="User password (hashed)"
    )
    email = models.EmailField(
        unique=True, 
        help_text="User's email address"
    )
    
    # Required fields for Django admin and authentication
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    class Meta:
        db_table = 'ecommerce_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return f"{self.username} ({self.email})"


class Product(models.Model):
    """
    Product model to store product information.
    """
    name = models.CharField(
        max_length=255, 
        help_text="Product name"
    )
    description = models.TextField(
        help_text="Detailed product description"
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        help_text="Product price (must be positive)"
    )
    stock = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0,
        help_text="Available stock quantity"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'ecommerce_product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} - ${self.price}"
    
    @property
    def is_in_stock(self):
        """Check if product is in stock"""
        return self.stock > 0


class Order(models.Model):
    """
    Order model to store order information.
    Each order belongs to a user and can contain multiple products.
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='orders',
        help_text="User who placed this order"
    )
    order_date = models.DateTimeField(
        auto_now_add=True,
        help_text="When the order was placed"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        help_text="Current order status"
    )
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        help_text="Total order amount"
    )
    
    class Meta:
        db_table = 'ecommerce_order'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-order_date']
    
    def __str__(self):
        return f"Order #{self.id} - {self.user.username} - ${self.total_amount}"
    
    def calculate_total(self):
        """Calculate total amount for this order"""
        total = sum(
            item.quantity * item.product.price 
            for item in self.order_items.all()
        )
        self.total_amount = total
        self.save()
        return total


class OrderProduct(models.Model):
    """
    Join table to handle many-to-many relationship between orders and products.
    This allows tracking quantity for each product in an order.
    """
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='order_items',
        help_text="Order this item belongs to"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='order_items',
        help_text="Product being ordered"
    )
    quantity = models.IntegerField(
        validators=[MinValueValidator(1)],
        help_text="Quantity of this product in the order"
    )
    price_at_time = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Price of the product when the order was placed"
    )
    
    class Meta:
        db_table = 'ecommerce_order_product'
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'
        unique_together = ['order', 'product']  # Prevent duplicate products in same order
    
    def __str__(self):
        return f"{self.quantity}x {self.product.name} in Order #{self.order.id}"
    
    def save(self, *args, **kwargs):
        """Override save to store current product price"""
        if not self.price_at_time:
            self.price_at_time = self.product.price
        super().save(*args, **kwargs)
    
    @property
    def subtotal(self):
        """Calculate subtotal for this order item"""
        return self.quantity * self.price_at_time