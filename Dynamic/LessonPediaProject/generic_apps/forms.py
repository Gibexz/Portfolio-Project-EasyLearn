from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from client.models import Client
from tutor.models import Tutor
from app_admin.models import AppAdmin


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


class TutorRegisterForm(UserCreationForm):
    """this class abstracts the tutor registration model"""
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
            'placeholder':'********',
            'id': 'pass'
        })

        self.fields['password2'].widget.attrs.update({
            'name':'confirm_password',
            'placeholder':'********',
            'id':'con_pass'
        })

        self.fields['area_of_specialization'].widget.attrs.update({
            'id': 'high_qual',
            'placeholder': 'enter your specialization'
        })

        self.fields['highest_qualification'].widget.attrs.update({
            
        })

    class Meta:
        model = Tutor
        fields = [
            'username', 'email', 'password1', 'password2', 'area_of_specialization', 'highest_qualification'
        ]


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
