#!/usr/bin/env python
"""
Script to populate the e-commerce database with sample data.
"""
import os
import sys
import django
from decimal import Decimal

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from django.contrib.auth import get_user_model
from ecommerce.models import Product, Order, OrderProduct

User = get_user_model()

def create_sample_data():
    """Create sample data for the e-commerce platform."""
    
    # Create sample users
    users_data = [
        {'username': 'john_doe', 'email': 'john@example.com', 'first_name': 'John', 'last_name': 'Doe'},
        {'username': 'jane_smith', 'email': 'jane@example.com', 'first_name': 'Jane', 'last_name': 'Smith'},
        {'username': 'bob_wilson', 'email': 'bob@example.com', 'first_name': 'Bob', 'last_name': 'Wilson'},
    ]
    
    created_users = []
    for user_data in users_data:
        user, created = User.objects.get_or_create(
            email=user_data['email'],
            defaults={
                'username': user_data['username'],
                'first_name': user_data['first_name'],
                'last_name': user_data['last_name']
            }
        )
        if created:
            user.set_password('password123')
            user.save()
            print(f"Created user: {user.username}")
        created_users.append(user)
    
    # Create sample products
    products_data = [
        {
            'name': 'Laptop Computer',
            'description': 'High-performance laptop perfect for work and gaming',
            'price': Decimal('999.99'),
            'stock': 15
        },
        {
            'name': 'Wireless Headphones',
            'description': 'Premium noise-canceling wireless headphones',
            'price': Decimal('199.99'),
            'stock': 25
        },
        {
            'name': 'Smartphone',
            'description': 'Latest model smartphone with advanced features',
            'price': Decimal('699.99'),
            'stock': 30
        },
        {
            'name': 'Coffee Maker',
            'description': 'Automatic coffee maker with programmable settings',
            'price': Decimal('89.99'),
            'stock': 12
        },
        {
            'name': 'Running Shoes',
            'description': 'Comfortable running shoes for all terrains',
            'price': Decimal('129.99'),
            'stock': 50
        },
        {
            'name': 'Desk Chair',
            'description': 'Ergonomic office chair with lumbar support',
            'price': Decimal('249.99'),
            'stock': 8
        },
    ]
    
    created_products = []
    for product_data in products_data:
        product, created = Product.objects.get_or_create(
            name=product_data['name'],
            defaults=product_data
        )
        if created:
            print(f"Created product: {product.name}")
        created_products.append(product)
    
    # Create sample orders
    if created_users and created_products:
        # Order 1: John buys laptop and headphones
        order1 = Order.objects.create(user=created_users[0], status='delivered')
        OrderProduct.objects.create(
            order=order1,
            product=created_products[0],  # Laptop
            quantity=1,
            price_at_time=created_products[0].price
        )
        OrderProduct.objects.create(
            order=order1,
            product=created_products[1],  # Headphones
            quantity=1,
            price_at_time=created_products[1].price
        )
        order1.calculate_total()
        print(f"Created order for {order1.user.username}: ${order1.total_amount}")
        
        # Order 2: Jane buys smartphone and coffee maker
        order2 = Order.objects.create(user=created_users[1], status='shipped')
        OrderProduct.objects.create(
            order=order2,
            product=created_products[2],  # Smartphone
            quantity=1,
            price_at_time=created_products[2].price
        )
        OrderProduct.objects.create(
            order=order2,
            product=created_products[3],  # Coffee Maker
            quantity=1,
            price_at_time=created_products[3].price
        )
        order2.calculate_total()
        print(f"Created order for {order2.user.username}: ${order2.total_amount}")
        
        # Order 3: Bob buys running shoes and desk chair
        order3 = Order.objects.create(user=created_users[2], status='processing')
        OrderProduct.objects.create(
            order=order3,
            product=created_products[4],  # Running Shoes
            quantity=2,  # Two pairs
            price_at_time=created_products[4].price
        )
        OrderProduct.objects.create(
            order=order3,
            product=created_products[5],  # Desk Chair
            quantity=1,
            price_at_time=created_products[5].price
        )
        order3.calculate_total()
        print(f"Created order for {order3.user.username}: ${order3.total_amount}")
    
    print("\nSample data creation completed!")
    print("You can now view the data in the Django admin at http://127.0.0.1:8000/admin/")

if __name__ == '__main__':
    create_sample_data()