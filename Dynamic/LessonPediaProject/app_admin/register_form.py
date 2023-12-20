from typing import Any
from django.contrib.auth.forms import UserCreationForm
from app_admin.models import AppAdmin


class AppAdminRegisterForm(UserCreationForm):
    """Register form for AppAdmin"""
    class Meta:
        model = AppAdmin
        fields = ['username', 'email', 'password1', 'password2']

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
