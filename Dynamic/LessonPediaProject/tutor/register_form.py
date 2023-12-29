from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from tutor.models import Tutor


class TutorRegisterForm(UserCreationForm):
    """this class abstracts the tutor registration model"""
    email = forms.EmailField(max_length=150, required=True, help_text='Enter Email')
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

        self.fields['primary_subject'].widget.attrs.update({
            'id': 'high_qual',
            'placeholder': 'enter first core subject',
        })

        self.fields['highest_qualification'].widget.attrs.update({
            
        })

    class Meta:
        model = Tutor
        fields = [
            'username', 'email', 'password1', 'password2', 'area_of_specialization', 'highest_qualification'
        ]
