from django.contrib.auth.backends import ModelBackend
from .models import AppAdmin


class AppAdminAuthBackend(ModelBackend):
    """Validation of appadmin login"""
    def authenticate(self, request, username=None, password=None, **kwargs):
        """"""
        try:
            user = AppAdmin.objects.get(email=username)
            if user.check_password(password):
                return user
            else:
                user = AppAdmin.objects.get(username=username)
                if user.check_password(password):
                    return user    
        except AppAdmin.DoesNotExist:
            None

    def get_user(self, user_id):
        try:
            return AppAdmin.objects.get(pk=user_id)
        except AppAdmin.DoesNotExist:
            return None