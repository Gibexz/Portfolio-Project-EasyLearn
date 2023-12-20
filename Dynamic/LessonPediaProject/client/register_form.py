from typing import Any
from django.contrib.auth.forms import UserCreationForm
from client.models import Client

class ClientRegisterForm(UserCreationForm):
    """Register form for client"""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter your email',
            }
        )
        self.fields['username'].widget.attrs.update(
            {
                'placeholder': 'Enter username',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': '********',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': '********',
            }
        )

    class Meta:
        model = Client
        fields = ['username', 'email', 'password1', 'password2']
