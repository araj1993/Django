#!/usr/bin/env python
"""
Script to verify the admin user login.
"""
import os
import sys
import django

# Configure Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

def verify_admin():
    """Verify admin user details and login."""
    
    print("=== ADMIN USER VERIFICATION ===")
    
    # Check if admin user exists
    try:
        admin_user = User.objects.get(username='admin')
        print("✅ Admin user found")
        print(f"   ID: {admin_user.id}")
        print(f"   Username: {admin_user.username}")
        print(f"   Email: {admin_user.email}")
        print(f"   Is Staff: {admin_user.is_staff}")
        print(f"   Is Superuser: {admin_user.is_superuser}")
        print(f"   Is Active: {admin_user.is_active}")
        
        # Test authentication (our custom user model uses email as USERNAME_FIELD)
        auth_user = authenticate(username='admin@ecommerce.com', password='admin123')
        if auth_user:
            print("✅ Password verification: SUCCESS")
            print(f"   Authenticated as: {auth_user.username} ({auth_user.email})")
            print("   Note: Login with email 'admin@ecommerce.com' and password 'admin123'")
        else:
            print("❌ Password verification: FAILED")
            
        # Also test direct password check
        password_check = admin_user.check_password('admin123')
        print(f"✅ Direct password check: {'SUCCESS' if password_check else 'FAILED'}")
            
    except User.DoesNotExist:
        print("❌ Admin user not found")
    
    # Show total users
    total_users = User.objects.count()
    print(f"\nTotal users in database: {total_users}")
    
    if total_users == 1:
        print("✅ Database contains only admin user")
    else:
        print("⚠️  Database contains multiple users:")
        for user in User.objects.all():
            print(f"   - {user.username} ({user.email})")

if __name__ == '__main__':
    verify_admin()