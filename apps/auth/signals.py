from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from rest_framework.response import Response
from rest_framework import status

@receiver(user_signed_up)
def user_signed_up_callback(request, user, **kwargs):
    return Response({"detail": "Registration successful"}, status=status.HTTP_200_OK)