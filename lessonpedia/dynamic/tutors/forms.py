from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  


class SignUpForm(UserCreationForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'type':"text",
            'name':"useremail",
            "placeholder":"enter email"
        })
        self.fields['username'].widget.attrs.update({
            'type':"text",
            'name':"username",
            "placeholder":"enter username"
        })
        self.fields['password1'].widget.attrs.update({
            'type':"text",
            'name':"password",
            "placeholder":"********"
        })
        self.fields['password2'].widget.attrs.update({
            'type':"text",
            'name':"password",
            "placeholder":"********"
        })

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
class SignUpTutor(UserCreationForm):
    """Tutors form basic"""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'type':"text",
            'name':"useremail",
            "placeholder":"enter email"
        })
        self.fields['username'].widget.attrs.update({
            'type':"text",
            'name':"username",
            "placeholder":"enter username"
        })
        self.fields['password1'].widget.attrs.update({
            'type':"text",
            'name':"password",
            "placeholder":"********"
        })
        self.fields['password2'].widget.attrs.update({
            'type':"text",
            'name':"password",
            "placeholder":"********"
        })

    specialization = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'type':"text",
        'name':"specialization",
        "placeholder":"enter specialization",
        'id':'specialization'
    }))
    qualification = forms.CharField(max_length=5)

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'email', 'password2', 'specialization', 'qualification'
        ]