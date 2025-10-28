# Django E-commerce Platform

A comprehensive Django-based e-commerce platform demonstrating model relationships, admin interface, and database management.

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Django 5.2.6
- pip (Python package installer)

### Installation & Setup

1. **Clone or navigate to the project directory**
   ```bash
   cd assignment10
   ```

2. **Install Django (if not already installed)**
   ```bash
   pip install django
   ```

3. **Apply database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser account**
   ```bash
   python manage.py createsuperuser
   ```
   - Username: `admin`
   - Email: `admin@example.com`
   - Password: `admin123` (or your choice)

5. **Create sample data (optional)**
   ```bash
   python manage.py shell -c "exec(open('create_sample_data.py').read())"
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Admin Interface: http://127.0.0.1:8000/admin/
   - Login with superuser credentials

## 📊 Project Structure

```
assignment10/
├── Ecom/                    # Main Django project
│   ├── settings.py          # Project configuration
│   ├── urls.py              # URL routing
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── store/                   # E-commerce app
│   ├── migrations/          # Database migrations
│   ├── models.py            # Data models
│   ├── admin.py             # Admin interface
│   ├── views.py             # View logic
│   └── urls.py              # App URLs
├── manage.py                # Django management commands
├── db.sqlite3               # SQLite database
├── create_sample_data.py    # Sample data script
├── PROJECT_DOCUMENTATION.md # Detailed documentation
└── README.md               # This file
```

## 🗃️ Database Models

### Product Model
- **Fields**: name, description, price, stock
- **Purpose**: Stores product information for the e-commerce store

### Order Model
- **Fields**: user (FK), order_date
- **Purpose**: Represents customer orders
- **Relationship**: Many-to-One with User

### OrderItem Model
- **Fields**: order (FK), product (FK), quantity
- **Purpose**: Individual items within an order
- **Relationships**: 
  - Many-to-One with Order
  - Many-to-One with Product

## 🔧 Features

- ✅ Complete Django project setup
- ✅ SQLite3 database configuration
- ✅ Model relationships with foreign keys
- ✅ Django admin interface integration
- ✅ Sample data for testing
- ✅ Proper URL routing
- ✅ Database migrations

## 📱 Admin Interface Features

Access the admin interface at `/admin/` to:

1. **Manage Products**
   - Add new products
   - Edit product details (name, description, price, stock)
   - Delete products

2. **Manage Orders**
   - View all orders
   - See order details and associated users
   - Track order dates

3. **Manage Order Items**
   - Add items to orders
   - Modify quantities
   - Associate products with orders

4. **User Management**
   - Create and manage user accounts
   - Assign orders to users

## 📄 Sample Data

The project includes a sample data script that creates:

- **4 Products**: Gaming Laptop, Wireless Mouse, Mechanical Keyboard, Gaming Headset
- **2 Users**: customer1 (John Doe), customer2 (Jane Smith)
- **2 Orders**: One for each customer
- **5 Order Items**: Distributed across the orders

Run the sample data script:
```bash
python manage.py shell -c "exec(open('create_sample_data.py').read())"
```

## 🔍 Testing the Relationships

1. **Product → OrderItem**: View how products appear in multiple orders
2. **Order → OrderItem**: See all items within a specific order
3. **User → Order**: Track all orders for a specific user

## 🛠️ Management Commands

```bash
# Check project for issues
python manage.py check

# Create new migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Access Django shell
python manage.py shell

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

# View migration status
python manage.py showmigrations
```

## 📈 Database Schema

| Model | Fields | Relationships |
|-------|---------|---------------|
| Product | id, name, description, price, stock | None |
| Order | id, user, order_date | FK → User |
| OrderItem | id, order, product, quantity | FK → Order, FK → Product |

## 🔒 Security Notes

- CSRF protection enabled
- Admin interface requires authentication
- Debug mode enabled (development only)
- SQLite database for development

## 📝 Next Steps

1. Add frontend templates and views
2. Implement customer registration and login
3. Create shopping cart functionality
4. Add payment processing
5. Implement order status tracking
6. Add product categories and search

## 🤝 Contributing

1. Make model changes in `store/models.py`
2. Create and apply migrations
3. Update admin interface in `store/admin.py`
4. Test changes through admin interface

## 📞 Support

For issues or questions:
1. Check Django documentation: https://docs.djangoproject.com/
2. Review project documentation: `PROJECT_DOCUMENTATION.md`
3. Verify database migrations are applied
4. Ensure superuser is created for admin access

---

**Project Created**: October 28, 2025  
**Django Version**: 5.2.6  
**Database**: SQLite3  
**Status**: Complete ✅