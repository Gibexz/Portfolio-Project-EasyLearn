from client.models import Client
from django.contrib.auth.forms import UserCreationForm

class ClientSignUpForm(UserCreationForm):
    """"""
    class Meta:
        model = Client
        fields = ('email', 'username', 'password1', 'password2')