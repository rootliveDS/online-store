from django.contrib import admin
from django.urls import path, include
from api.v1.auth.views import CustomRegisterView

urlpatterns = [
    path('api/auth/', include('dj_rest_auth.urls')),
    # path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/auth/registration/', CustomRegisterView.as_view(), name='rest_register'),

]


