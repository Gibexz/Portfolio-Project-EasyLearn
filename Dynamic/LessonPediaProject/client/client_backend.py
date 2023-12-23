# Authentication backend for Client login validation.

from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.backends import ModelBackend
from .models import Client

class ClientAuthBackend(ModelBackend):
    """Custom backend for Client login validation."""
    def authenticate(self, request, username_or_email=None, password=None, **kwargs):
        """
        Validates a user using email or password.
        Client: The authenticated Client object or None if authentication fails.
        """
        try:
            validate_email(username_or_email)
            is_valid_email_format = True
        except ValidationError:
            is_valid_email_format = False
        
        auth_type = 'email' if is_valid_email_format else 'username'
        auth_param = {auth_type: username_or_email}
        
        try:
            client = Client.objects.get(**auth_param)
            if client.check_password(password):
                return client
        except Client.DoesNotExist:
            pass

        return None
