# Online Store

**Online Store** is a Django-based web application designed for an online store. This project is structured according to best practices and is Dockerized for easy setup and deployment.

## Features

- **User Authentication and Registration**: Includes login, logout, password reset, and user profile management.
- **Product Management**: Create, update, and delete product listings.
- **Cart Functionality**: Users can add products to their cart and view cart details.
- **Order Processing**: Supports a checkout process, including payment and order review.
- **Admin Panel**: Comprehensive Django admin panel for managing all aspects of the store.

## Technologies

- **Django 5.x**
- **PostgreSQL**
- **Docker**
- **Gunicorn**

## Requirements

- **Docker**: Make sure Docker is installed and running on your machine.
- **Docker Compose**: Required for building and orchestrating the Docker containers.

## Quick Start

### 1. Clone the Repository

git clone https://github.com/username/myproject.git
cd online-store

###  2. Build and Start the Application

docker-compose up --build

###  3. Apply Migrations

docker-compose exec web python manage.py migrate

###  4. Create a Superuser

docker-compose exec web python manage.py createsuperuser

# API Endpoints
    admin/: Django admin panel.

    api/auth/password/reset/: Password reset endpoint. [name='rest_password_reset']

    api/auth/password/reset/confirm/: Confirm password reset. [name='rest_password_reset_confirm']

    api/auth/login/: Login endpoint. [name='rest_login']

    api/auth/logout/: Logout endpoint. [name='rest_logout']

    api/auth/user/: User details endpoint. [name='rest_user_details']

    api/auth/password/change/: Password change endpoint. [name='rest_password_change']

    api/auth/registration/: User registration endpoint. [name='rest_register']

    api/categories/: List of product categories. [name='category-list']

    api/products/: List of products. [name='product-list']

    api/products/<int:pk>/: Product detail view. [name='product-detail']

    api/cart/: Cart details view. [name='cart-detail']

    api/add-cart/: Add a product to the cart. [name='add-cart']

    api/checkout/: Checkout process. [name='checkout']

    api/reviews/: List of product reviews. [name='reviews-list']

    api/add-review/: Add a product review. [name='add-review']

    ^api/media/(?P<path>.*)$: Serve media files.
