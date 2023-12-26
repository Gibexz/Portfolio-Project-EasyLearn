#Tutors authentication backend logic

from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.backends import ModelBackend
from .models import Tutor

class TutorAuthBackend(ModelBackend):
    """validates a tutor for login"""
    def authenticate(self, request, username_or_email=None, password=None, **kwargs):
        """
        Validates a tutor using email or password.
       Returns the authenticated tutor object or None if authentication fails.
        """
        print(f"Attempting to authenticate: {username_or_email}")
        try:
            validate_email(username_or_email)
            is_valid_email_format = True
        except ValidationError:
            is_valid_email_format = False

        auth_type = 'email__iexact' if is_valid_email_format else 'username__iexact' # doing email__iexact=username_or_email will make it case insensitive but i think django handles that for us
        auth_param = {auth_type: username_or_email}

        try:
            tutor = Tutor.objects.get(**auth_param) # Tutor.objects.get(email=username_or_email) [or username=username_or_email]
            if tutor.check_password(password):
                print(f"Authenticated: {tutor}")
                print(f'Is_authenticated: {tutor.is_authenticated}')
                return tutor
        except Tutor.DoesNotExist:
            pass

        return None
    
    def get_user(self, user_id):
        """
        Returns the tutor object using the given user_id.
        """
        try:
            return Tutor.objects.get(pk=user_id)
        except Tutor.DoesNotExist:
            return None
