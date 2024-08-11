from django.urls import path, include
from api.v1.auth.views import CustomRegisterView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/', CustomRegisterView.as_view(), name='rest_register'),

]


