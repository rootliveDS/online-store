import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User


@pytest.fixture
def api_client():
    return APIClient()


# @pytest.mark.django_db
# def test_registration(api_client):
#     url = reverse('rest_register')
#     data = {
#         'username': 'testuser',
#         'email': 'testuser@example.com',
#         'password1': 'TestPassword123',
#         'password2': 'TestPassword123'
#     }
#     response = api_client.post(url, data)
#     assert response.status_code == status.HTTP_201_CREATED
#     assert User.objects.filter(username='testuser').exists()


@pytest.mark.django_db
def test_registration(api_client):
    url = '/api/auth/registration/'
    data = {
        'username': 'testuser',
        'password1': 'TestPassword123',
        'password2': 'TestPassword123',
        'email': 'testuser@example.com'
    }
    response = api_client.post(url, data, format='json')  # Убедитесь, что формат указан
    print("Response status code:", response.status_code)
    print("Response data:", response.data)
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.filter(username='testuser').exists()


@pytest.mark.django_db
def test_login(api_client):
    user = User.objects.create_user(username='testuser', password='TestPassword123', email='testuser@example.com')

    url = reverse('rest_login')
    data = {
        'username': 'testuser',
        'password': 'TestPassword123'
    }
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_200_OK
    assert 'key' in response.data


@pytest.mark.django_db
def test_logout(api_client):
    user = User.objects.create_user(username='testuser', password='TestPassword123', email='testuser@example.com')

    login_url = reverse('rest_login')
    login_data = {
        'username': 'testuser',
        'password': 'TestPassword123'
    }
    login_response = api_client.post(login_url, login_data)
    assert login_response.status_code == status.HTTP_200_OK

    token = login_response.data['key']
    api_client.credentials(HTTP_AUTHORIZATION='Token ' + token)

    logout_url = reverse('rest_logout')
    logout_response = api_client.post(logout_url)
    assert logout_response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_user(api_client):
    user = User.objects.create_user(username='testuser', password='TestPassword123', email='testuser@example.com')

    login_url = reverse('rest_login')
    login_data = {
        'username': 'testuser',
        'password': 'TestPassword123'
    }
    login_response = api_client.post(login_url, login_data)
    assert login_response.status_code == status.HTTP_200_OK

    token = login_response.data['key']
    api_client.credentials(HTTP_AUTHORIZATION='Token ' + token)

    user_url = reverse('rest_user_details')
    user_response = api_client.get(user_url)
    assert user_response.status_code == status.HTTP_200_OK
    assert user_response.data['username'] == 'testuser'
    assert user_response.data['email'] == 'testuser@example.com'
