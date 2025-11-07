from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	stock = models.IntegerField()

	def __str__(self):
		return self.name

class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	order_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Order {self.id} by {self.user.username}"
	
	def get_total(self):
		"""Calculate the total price of the order"""
		total = 0
		for item in self.items.all():
			total += item.get_total_price()
		return total

class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField()

	def __str__(self):
		return f"{self.quantity} x {self.product.name}"
	
	def get_total_price(self):
		"""Calculate the total price for this order item"""
		return self.product.price * self.quantity
