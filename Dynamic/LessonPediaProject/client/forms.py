from .models import Client
from django.contrib.auth.forms import UserCreationForm


class ClientRegistration(UserCreationForm):
    """Logics for client registration"""

    class Meta:
        model = Client
        fields = [
            'username', 'email', 'password1', 'password2'
        ]