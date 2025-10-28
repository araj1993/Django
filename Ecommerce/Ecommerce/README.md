# Project Completion Report – Ecom (Django E-commerce Application)

### 1. Project Setup

      - A new Django project named Ecom was created using the command:
       **django-admin startproject Ecom**

      - An application named store was created within the project using:
       **python manage.py startapp store**

      - The store app was successfully added to the INSTALLED_APPS section in settings.py.
       

### 2. URL Configuration

      - The store app’s URLs were included in the main project’s URL configuration file (Ecom/urls.py).

      - A dedicated urls.py file was created inside the store application folder to manage its URL routing.

### 3. Model Creation

      - Models were defined in store/models.py according to the provided schema.

      - Appropriate ForeignKey relationships were established between models to ensure data integrity and relational consistency.

### 4. Database Setup

      - The project was configured to use SQLite3 as the database backend.

      - Database migrations were created and applied successfully to generate the necessary tables in the database.

### 5. Admin Interface

      - All created models were registered in the Django admin site to enable easy data management.

      - Admin access was verified and functional.

### 6. Testing

      - Sample users, products, and orders were added through the admin interface.

      - The database schema and model relationships were validated successfully based on test entries.

## Database Schema

### Product Table

| Field Name | Type | Description |
|------------|------|-------------|
| id | Primary Key | Unique identifier for each product |
| name | String | Name of the product |
| description | Text | Detailed product description |
| price | Decimal | Price of the product |
| stock | Integer | Quantity available in stock |

### Order Table

| Field Name | Type | Description |
|------------|------|-------------|
| id | Primary Key | Unique identifier for each order |
| user | Foreign Key (User) | References the user who placed the order |
| order_date | Timestamp | Date and time when the order was created |

### OrderItem Table

| Field Name | Type | Description |
|------------|------|-------------|
| id | Primary Key | Unique identifier for each order item |
| order | Foreign Key (Order) | References the related order |
| product | Foreign Key (Product) | References the purchased product |
| quantity | Integer | Quantity of the product ordered |

