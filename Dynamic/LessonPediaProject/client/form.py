from client.models import Client
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class ClientSignUpForm(UserCreationForm):
    """"""
    class Meta:
        model = Client
        fields = ('email', 'username', 'password1', 'password2')

class ClientSignInForm(AuthenticationForm):
    """Authenticating user for login"""
    
    class Meta:
        model = Client
        fields = [
            'username', 'password'
        ]