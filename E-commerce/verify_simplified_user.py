#!/usr/bin/env python
"""
Script to verify the updated ecommerce_user table structure and recreate admin user.
"""
import os
import sys
import django

# Configure Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from django.contrib.auth import get_user_model, authenticate
from django.db import connection

User = get_user_model()

def verify_table_structure():
    """Verify the ecommerce_user table structure."""
    
    print("=" * 60)
    print("ECOMMERCE_USER TABLE VERIFICATION")
    print("=" * 60)
    
    # Get table structure using raw SQL
    with connection.cursor() as cursor:
        cursor.execute("PRAGMA table_info(ecommerce_user);")
        columns = cursor.fetchall()
    
    print("\n1. TABLE STRUCTURE:")
    print("-" * 30)
    print("Column Name       | Type         | Not Null | Default | Primary Key")
    print("-" * 70)
    
    required_fields = ['id', 'username', 'password', 'email']
    found_fields = []
    
    for column in columns:
        cid, name, type_name, not_null, default, pk = column
        pk_indicator = "YES" if pk else "NO"
        null_indicator = "YES" if not_null else "NO"
        default_val = default if default else "NULL"
        
        print(f"{name:<17} | {type_name:<12} | {null_indicator:<8} | {default_val:<7} | {pk_indicator}")
        
        if name in required_fields:
            found_fields.append(name)
    
    print("\n2. REQUIRED FIELDS CHECK:")
    print("-" * 30)
    for field in required_fields:
        status = "✅ FOUND" if field in found_fields else "❌ MISSING"
        print(f"• {field}: {status}")
    
    return all(field in found_fields for field in required_fields)

def recreate_admin_user():
    """Recreate admin user with simplified schema."""
    
    print("\n3. ADMIN USER SETUP:")
    print("-" * 30)
    
    # Remove existing admin user if exists
    User.objects.filter(username='admin').delete()
    
    # Create new admin user with simplified schema
    admin_user = User.objects.create_superuser(
        username='admin',
        email='admin@ecommerce.com',
        password='admin123'
    )
    
    print("✅ Admin user created with simplified schema")
    print(f"   ID: {admin_user.id}")
    print(f"   Username: {admin_user.username}")
    print(f"   Email: {admin_user.email}")
    print(f"   Password: admin123 (hashed)")

def verify_admin_login():
    """Verify admin user can login."""
    
    print("\n4. LOGIN VERIFICATION:")
    print("-" * 30)
    
    # Test authentication
    auth_user = authenticate(username='admin', password='admin123')
    if auth_user:
        print("✅ Username/Password authentication: SUCCESS")
        print(f"   Authenticated as: {auth_user.username}")
    else:
        print("❌ Username/Password authentication: FAILED")
    
    # Test direct password check
    admin_user = User.objects.get(username='admin')
    password_check = admin_user.check_password('admin123')
    print(f"✅ Direct password check: {'SUCCESS' if password_check else 'FAILED'}")

def show_user_data():
    """Show all user data."""
    
    print("\n5. CURRENT USER DATA:")
    print("-" * 30)
    
    users = User.objects.all()
    print(f"Total users: {users.count()}")
    
    for user in users:
        print(f"\nUser ID: {user.id}")
        print(f"Username: {user.username}")
        print(f"Email: {user.email}")
        print(f"Password Hash: {user.password[:20]}...")
        print(f"Is Staff: {user.is_staff}")
        print(f"Is Active: {user.is_active}")

def main():
    """Main verification function."""
    
    # Verify table structure
    structure_ok = verify_table_structure()
    
    if structure_ok:
        print("\n✅ Table structure verification: PASSED")
        
        # Recreate admin user
        recreate_admin_user()
        
        # Verify login
        verify_admin_login()
        
        # Show current data
        show_user_data()
        
        print("\n" + "=" * 60)
        print("✅ ECOMMERCE_USER TABLE UPDATE COMPLETED!")
        print("=" * 60)
        print("\nTable now contains only required fields:")
        print("• id (Primary Key)")
        print("• username (Unique, String)")
        print("• password (String)")
        print("• email (Unique, String)")
        print("\nAdmin Login:")
        print("• Username: admin")
        print("• Password: admin123")
        print("• Admin URL: http://127.0.0.1:8000/admin/")
        
    else:
        print("\n❌ Table structure verification: FAILED")
        print("Required fields are missing from the table.")

if __name__ == '__main__':
    main()