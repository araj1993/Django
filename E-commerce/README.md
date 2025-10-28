# E-commerce Database Project

A Django-based e-commerce platform with a complete database design for managing users, products, and orders.

## Project Overview

This project implements a relational database system for an e-commerce platform using Django ORM. The system manages:

- **Users**: Customer accounts with authentication
- **Products**: Product catalog with inventory management
- **Orders**: Order processing and tracking
- **Order Items**: Many-to-many relationship between orders and products

## Database Schema

### User Table
- `id` (Primary Key)
- `username` (Unique, String)
- `password` (String, hashed)
- `email` (Unique, String)
- Additional Django user fields (first_name, last_name, etc.)

### Product Table
- `id` (Primary Key)
- `name` (String)
- `description` (Text)
- `price` (Decimal)
- `stock` (Integer)
- `created_at` (Timestamp)
- `updated_at` (Timestamp)

### Order Table
- `id` (Primary Key)
- `user_id` (Foreign Key → User)
- `order_date` (Timestamp)
- `status` (String: pending, processing, shipped, delivered, cancelled)
- `total_amount` (Decimal)

### Order_Product Table (Join Table)
- `id` (Primary Key)
- `order_id` (Foreign Key → Order)
- `product_id` (Foreign Key → Product)
- `quantity` (Integer)
- `price_at_time` (Decimal) - Price when order was placed

## Features

### Database Features
- **Foreign Key Relationships**: Proper referential integrity
- **Data Validation**: Price/quantity validation, email uniqueness
- **Automatic Timestamps**: Track creation and modification times
- **Price History**: Store product prices at time of purchase
- **Stock Management**: Track inventory levels

### Django Features
- **Custom User Model**: Email-based authentication
- **Admin Interface**: Complete admin panel for data management
- **Model Methods**: Business logic (calculate totals, check stock)
- **Relationships**: Proper Django model relationships

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Installation

1. **Clone/Navigate to the project directory**
   ```bash
   cd "C:\Users\KIRAN\Documents\araj1993-git\Django\E-commerce"
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install Django
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (admin)**
   ```bash
   python create_superuser.py
   ```

6. **Load sample data**
   ```bash
   python populate_data.py
   ```

7. **Start development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin interface: http://127.0.0.1:8000/admin/
   - Admin credentials: admin@ecommerce.com / admin123

## Project Structure

```
E-commerce/
├── manage.py                 # Django management script
├── create_superuser.py      # Script to create admin user
├── populate_data.py         # Script to load sample data
├── db.sqlite3              # SQLite database file
├── ecommerce_project/      # Main project directory
│   ├── __init__.py
│   ├── settings.py         # Django settings
│   ├── urls.py            # URL routing
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
├── ecommerce/              # Main application
│   ├── __init__.py
│   ├── models.py          # Database models
│   ├── admin.py           # Admin interface configuration
│   ├── views.py           # View functions
│   ├── urls.py            # App URL routing
│   ├── apps.py            # App configuration
│   ├── tests.py           # Unit tests
│   └── migrations/        # Database migration files
└── static/                # Static files directory
```

## Database Relationships

```
User (1) ←→ (Many) Order
Order (1) ←→ (Many) OrderProduct ←→ (1) Product
```

### Relationship Details:
- **User → Order**: One-to-Many (One user can have multiple orders)
- **Order → OrderProduct**: One-to-Many (One order can contain multiple products)
- **Product → OrderProduct**: One-to-Many (One product can be in multiple orders)
- **Order ↔ Product**: Many-to-Many through OrderProduct (with additional fields)

## Sample Data

The project includes sample data with:
- 3 sample users (john_doe, jane_smith, bob_wilson)
- 6 sample products (electronics, furniture, shoes, etc.)
- 3 sample orders with multiple items each

## Key Model Features

### User Model
- Custom user model extending Django's AbstractUser
- Email as primary identifier
- Unique email and username constraints

### Product Model
- Price validation (must be positive)
- Stock tracking with inventory management
- Timestamps for creation and updates
- `is_in_stock` property for quick stock checks

### Order Model
- Status tracking (pending → processing → shipped → delivered)
- Automatic total calculation
- Related name for easy access to order items

### OrderProduct Model
- Quantity validation (minimum 1)
- Price history (stores price at time of order)
- Unique constraint (one entry per product per order)
- Automatic subtotal calculation

## Admin Interface Features

- **User Management**: Complete user administration
- **Product Management**: Inventory tracking, bulk price updates
- **Order Management**: Order status updates, inline item editing
- **Order Items**: Direct management of order-product relationships
- **Reporting**: List views with filtering and searching

## Security Considerations

- Passwords are hashed using Django's authentication system
- CSRF protection enabled
- SQL injection protection through Django ORM
- Input validation on all model fields

## Future Enhancements

Potential extensions to the database schema:
- **Categories**: Product categorization
- **Reviews**: Customer product reviews
- **Coupons**: Discount system
- **Addresses**: Shipping address management
- **Payment**: Payment method tracking
- **Inventory**: Advanced inventory management

## Development Notes

- Uses SQLite for development (easily configurable for PostgreSQL/MySQL)
- Follows Django best practices for model design
- Includes comprehensive admin interface
- Sample data for testing and development
- Ready for production deployment with minimal configuration changes

## Contact

For questions or suggestions about the database design, please refer to the Django documentation or create an issue in the project repository.