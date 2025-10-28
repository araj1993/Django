#!/usr/bin/env python
"""
Demo script to showcase the e-commerce database relationships and queries.
"""
import os
import sys
import django

# Configure Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from django.contrib.auth import get_user_model
from ecommerce.models import Product, Order, OrderProduct
from django.db.models import Sum, Count, F

User = get_user_model()

def run_database_queries():
    """Demonstrate various database queries and relationships."""
    
    print("=" * 60)
    print("E-COMMERCE DATABASE DEMONSTRATION")
    print("=" * 60)
    
    # 1. Show all users
    print("\n1. USERS IN THE SYSTEM:")
    print("-" * 30)
    users = User.objects.all()
    for user in users:
        print(f"• {user.username} ({user.email}) - {user.first_name} {user.last_name}")
    
    # 2. Show all products with stock info
    print("\n2. PRODUCT CATALOG:")
    print("-" * 30)
    products = Product.objects.all()
    for product in products:
        stock_status = "✓ In Stock" if product.is_in_stock else "✗ Out of Stock"
        print(f"• {product.name}: ${product.price} - Stock: {product.stock} {stock_status}")
    
    # 3. Show all orders with details
    print("\n3. ORDER HISTORY:")
    print("-" * 30)
    orders = Order.objects.select_related('user').prefetch_related('order_items__product')
    for order in orders:
        print(f"\nOrder #{order.id} - {order.user.username} - {order.status.upper()}")
        print(f"  Date: {order.order_date.strftime('%Y-%m-%d %H:%M')}")
        print(f"  Total: ${order.total_amount}")
        print("  Items:")
        for item in order.order_items.all():
            subtotal = item.quantity * item.price_at_time
            print(f"    - {item.quantity}x {item.product.name} @ ${item.price_at_time} = ${subtotal}")
    
    # 4. Demonstrate relationships - User's orders
    print("\n4. USER ORDER ANALYSIS:")
    print("-" * 30)
    for user in User.objects.filter(orders__isnull=False).distinct():
        order_count = user.orders.count()
        total_spent = user.orders.aggregate(total=Sum('total_amount'))['total'] or 0
        print(f"• {user.username}: {order_count} orders, Total spent: ${total_spent}")
    
    # 5. Product popularity analysis
    print("\n5. PRODUCT POPULARITY:")
    print("-" * 30)
    product_stats = OrderProduct.objects.values('product__name').annotate(
        total_sold=Sum('quantity'),
        times_ordered=Count('order', distinct=True)
    ).order_by('-total_sold')
    
    for stat in product_stats:
        print(f"• {stat['product__name']}: {stat['total_sold']} units sold in {stat['times_ordered']} orders")
    
    # 6. Show current inventory after orders
    print("\n6. INVENTORY STATUS:")
    print("-" * 30)
    for product in Product.objects.all():
        total_sold = OrderProduct.objects.filter(product=product).aggregate(
            sold=Sum('quantity'))['sold'] or 0
        print(f"• {product.name}: {product.stock} in stock, {total_sold} sold")
    
    # 7. Advanced query - Orders with multiple items
    print("\n7. MULTI-ITEM ORDERS:")
    print("-" * 30)
    multi_item_orders = Order.objects.annotate(
        item_count=Count('order_items')
    ).filter(item_count__gt=1)
    
    for order in multi_item_orders:
        print(f"• Order #{order.id}: {order.item_count} different products, Total: ${order.total_amount}")
    
    # 8. Show database statistics
    print("\n8. DATABASE STATISTICS:")
    print("-" * 30)
    print(f"• Total Users: {User.objects.count()}")
    print(f"• Total Products: {Product.objects.count()}")
    print(f"• Total Orders: {Order.objects.count()}")
    print(f"• Total Order Items: {OrderProduct.objects.count()}")
    print(f"• Average Order Value: ${Order.objects.aggregate(avg=Sum('total_amount'))['avg'] / Order.objects.count():.2f}")
    
    print("\n" + "=" * 60)
    print("Database demonstration completed!")
    print("Access the admin interface at: http://127.0.0.1:8000/admin/")
    print("Login: admin@ecommerce.com | Password: admin123")
    print("=" * 60)

if __name__ == '__main__':
    run_database_queries()