from dj_rest_auth.registration.views import RegisterView
from rest_framework.response import Response
from rest_framework import status

class CustomRegisterView(RegisterView):
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == 204:
            response.status_code = status.HTTP_201_CREATED
            response.data = {"detail": "Registration successful"}
        return response