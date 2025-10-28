#!/usr/bin/env python
"""
Script to clean up the e_commerce_user table and keep only admin user.
"""
import os
import sys
import django

# Configure Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from django.contrib.auth import get_user_model
from ecommerce.models import Order, OrderProduct

User = get_user_model()

def cleanup_users():
    """Remove all users except admin and update admin credentials."""
    
    print("Starting user cleanup...")
    
    # First, delete all orders and order items from non-admin users
    print("Cleaning up orders from non-admin users...")
    non_admin_users = User.objects.exclude(username='admin')
    
    for user in non_admin_users:
        # Delete all orders for this user (this will cascade to OrderProduct)
        user_orders = Order.objects.filter(user=user)
        order_count = user_orders.count()
        if order_count > 0:
            print(f"Deleting {order_count} orders for user {user.username}")
            user_orders.delete()
    
    # Delete all non-admin users
    deleted_count = non_admin_users.count()
    if deleted_count > 0:
        print(f"Deleting {deleted_count} non-admin users...")
        non_admin_users.delete()
    
    # Update admin user credentials
    try:
        admin_user = User.objects.get(username='admin')
        admin_user.set_password('admin123')
        admin_user.email = 'admin@ecommerce.com'
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.is_active = True
        admin_user.save()
        print("✅ Updated admin user credentials")
    except User.DoesNotExist:
        # Create admin user if doesn't exist
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@ecommerce.com',
            password='admin123'
        )
        print("✅ Created new admin user")
    
    # Verify final state
    print("\nFinal user state:")
    users = User.objects.all()
    for user in users:
        print(f"- Username: {user.username}")
        print(f"  Email: {user.email}")
        print(f"  Is Staff: {user.is_staff}")
        print(f"  Is Superuser: {user.is_superuser}")
        print(f"  Is Active: {user.is_active}")
    
    print(f"\nTotal users in database: {User.objects.count()}")
    print(f"Total orders in database: {Order.objects.count()}")
    print(f"Total order items in database: {OrderProduct.objects.count()}")
    
    print("\n✅ User cleanup completed!")
    print("Admin credentials:")
    print("  Username: admin")
    print("  Password: admin123")
    print("  Email: admin@ecommerce.com")

if __name__ == '__main__':
    cleanup_users()