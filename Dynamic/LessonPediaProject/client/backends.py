from django.contrib.auth.backends import ModelBackend
from .models import Client
import re

class EmailClientBackend(ModelBackend):
    """Use the backend to validate use with email"""

    @staticmethod
    def is_valid_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def authenticate(self, request, username=None, password=None, **kwargs):
        is_email = self.is_valid_email(username)

        if is_email:
            try:
                user = Client.objects.get(email=username)
            except Client.DoesNotExist:
                return None
        else:
            try:
                user = Client.objects.get(username=username)
            except Client.DoesNotExist:
                return None

        if user.check_password(password):
            return user

    def get_user(self, user_id):
        try:
            return Client.objects.get(pk=user_id)
        except Client.DoesNotExist:
            return None