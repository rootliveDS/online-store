import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apps.shop.models import Category, Product, Cart, Order, Review, CartItem
from django.contrib.auth.models import User

@pytest.fixture
def api_client():
    return APIClient()

def create_user(api_client):
    user = User.objects.create_user(username='testuser', password='testpass')
    api_client.login(username='testuser', password='testpass')
    return user

@pytest.mark.django_db
def test_category_list_view(api_client):
    create_user(api_client)
    Category.objects.create(name='Category 1')
    Category.objects.create(name='Category 2')

    url = reverse('category-list')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2

@pytest.mark.django_db
def test_product_list_view(api_client):
    create_user(api_client)
    category = Category.objects.create(name='Category 1')
    Product.objects.create(name='Product 1', category=category, price='10.00')

    url = reverse('product-list')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1

@pytest.mark.django_db
def test_product_detail_view(api_client):
    create_user(api_client)
    category = Category.objects.create(name='Test Category')
    product = Product.objects.create(name='Product 1', price=10.00, category=category)

    url = reverse('product-detail', args=[product.pk])
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == product.name

@pytest.mark.django_db
def test_cart_detail_view(api_client):
    user = create_user(api_client)
    Cart.objects.create(user=user)

    url = reverse('cart-detail')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['user'] == user.id

@pytest.mark.django_db
def test_checkout_view(api_client):
    user = create_user(api_client)
    Cart.objects.create(user=user)

    url = reverse('checkout')
    response = api_client.post(url)

    assert response.status_code == status.HTTP_201_CREATED
    assert Order.objects.filter(user=user).exists()

@pytest.mark.django_db
def test_add_review_view(api_client):
    user = create_user(api_client)
    category = Category.objects.create(name='Category 1')
    product = Product.objects.create(name='Product 1', price=10.00, category=category)

    url = reverse('add-review')
    data = {
        'product': product.pk,
        'rating': 5,
        'comment': 'Great product!'
    }
    response = api_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert Review.objects.filter(user=user, product=product).exists()

@pytest.mark.django_db
def test_reviews_list_view(api_client):
    category = Category.objects.create(name='Category 1')
    product = Product.objects.create(name='Product 1', price=10.00, category=category)
    user = create_user(api_client)
    Review.objects.create(product=product, rating=5, comment='Great!', user=user)

    url = reverse('reviews-list')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1

@pytest.mark.django_db
def test_add_to_cart_view(api_client):
    user = create_user(api_client)
    category = Category.objects.create(name='Category 1')
    product = Product.objects.create(name='Product 1', price=10.00, category=category)

    url = reverse('add-cart')
    data = {
        'product_id': product.pk,
        'quantity': 2
    }
    response = api_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert CartItem.objects.filter(cart__user=user, product=product).exists()
    cart_item = CartItem.objects.get(cart__user=user, product=product)
    assert cart_item.quantity == 2
