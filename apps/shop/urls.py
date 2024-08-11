from django.urls import path
from api.v1.shop.views import CategoryListView, ProductListView, ProductDetailView, CartDetailView, CheckoutView, ReviewsListView, AddReviewView, AddToCartView
urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('cart/', CartDetailView.as_view(), name='cart-detail'),
    path('add-cart/', AddToCartView.as_view(), name='add-cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('reviews/', ReviewsListView.as_view(), name='reviews-list'),
    path('add-review/', AddReviewView.as_view(), name='add-review'),
]
