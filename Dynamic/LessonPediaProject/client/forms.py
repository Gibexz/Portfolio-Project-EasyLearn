from typing import Any
from .models import Client
from django.contrib.auth.forms import UserCreationForm


class ClientRegistration(UserCreationForm):
    """Logics for client registration"""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'name':'username',
            'placeholder':'enter username'
        })

        self.fields['email'].widget.attrs.update({
            'name':'email',
            'placeholder':'enter email'
        })

        self.fields['password1'].widget.attrs.update({
            'name':'password',
            'placeholder':'********'
        })

        self.fields['password2'].widget.attrs.update({
            'name':'confirm_password',
            'placeholder':'********'
        })

    class Meta:
        model = Client
        fields = [
            'username', 'email', 'password1', 'password2'
        ]
