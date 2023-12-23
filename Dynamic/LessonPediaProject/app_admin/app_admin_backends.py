# AppAdmin authentication backends
from django.contrib.auth.backends import ModelBackend
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import AppAdmin


class AppAdminAuthBackend(ModelBackend):
    """Backend for LessonPedia Admin authentication"""
    def authenticate(self, request, username_or_email=None, password=None, **kwargs):
        '''use provided email or username along with password to validate user
        return a user object or None if validation fails
        '''
        try:
            validate_email(username_or_email)
            is_valid_email_format = True
        except ValidationError:
            is_valid_email_format = False
        
        auth_type = 'email' if is_valid_email_format else 'username'
        auth_param = {auth_type: username_or_email}

        try:
            admin = AppAdmin.objects.get(**auth_param)
            if admin.check_password(password):
                return admin
        except AppAdmin.DoesNotExist:
            pass

        return None