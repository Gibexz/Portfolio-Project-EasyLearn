from .models import Client
from django.contrib.auth.backends import ModelBackend

class EmailClientBackend(ModelBackend):
    """Use the backend to validate use with email"""
    def mail_authentication(self, request, username=None, password=None, **kwargs): 
        try:
            user = Client.objects.get(email=username)
            if user.check_password(password):
                return user
        except Client.DoesNotExist:
            return None
        
    def username_authenticate(self, request, username=None, password=None, **kwargs): 
        try:
            user = Client.objects.get(username=username)
            if user.check_password(password):
                return user
        except Client.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Client.objects.get(pk=user_id)
        except Client.DoesNotExist:
            return None