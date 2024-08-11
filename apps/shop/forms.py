from django import forms
from .models import Product, CartItem, Order, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'image', 'stock']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['product', 'rating', 'comment']
