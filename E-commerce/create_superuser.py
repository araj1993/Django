#!/usr/bin/env python
"""
Script to create a superuser for the e-commerce platform.
Run this after setting up the database.
"""
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

def create_superuser():
    """Create a superuser if one doesn't exist."""
    if not User.objects.filter(is_superuser=True).exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@ecommerce.com',
            password='admin123'  # Change this in production!
        )
        print("Superuser created successfully!")
        print("Username: admin")
        print("Email: admin@ecommerce.com")
        print("Password: admin123")
        print("\nIMPORTANT: Please change the default password in production!")
    else:
        print("Superuser already exists.")

if __name__ == '__main__':
    create_superuser()