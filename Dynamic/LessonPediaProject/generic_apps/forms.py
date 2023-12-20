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
    """Register form for tutor"""
    area_of_specialization = forms.CharField(max_length=100, required=True, help_text='Enter your area of specialization')
    def __init__(self, *args, **kwargs):
        super(TutorRegisterForm, self).__init__(*args, **kwargs)
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

        # self.fields['area_of_specialization'].widget.attrs.update(
        #     {
        #         'placeholder': 'Enter specialty',
        #     }
        # )

    class Meta:
        model = Tutor
        fields = ['username', 'email', 'password1', 'password2', 'highest_qualification']



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
