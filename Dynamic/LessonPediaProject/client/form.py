from typing import Any
from client.models import Client
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


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

class UserProfileRegistrationForm(forms.ModelForm):
    """Update user profile form"""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({
            'id':'firstName',
            'placeholder':"First Name",
            'requires':'required'
        })
        self.fields["last_name"].widget.attrs.update({
            'id':'lastName',
            'placeholder':"Last Name",
            'required':'required'
        })
        self.fields["others"].widget.attrs.update({
            'id':'others',
            'placeholder':"Other Names",
        })
        self.fields["residential_address"].widget.attrs.update({
            'id':'address',
            'placeholder':"Address",
            'required': 'required'
        })
        self.fields["state_of_residence"].widget.attrs.update({
            'id':'state',
            'placeholder':"State of Resident",
            'required': 'required'
        })
        self.fields["nationality"].widget.attrs.update({
            'id':'nationality',
            'placeholder':"Nationality",
            'required': 'required'
        })
        self.fields["phone_number"].widget.attrs.update({
            'id':'phoneNumber',
            'placeholder':"Phone Number",
            'required': 'required'
        })
        
    class Meta:
        model = Client
        fields = [
            'first_name',
            'last_name',
            'others',
            'phone_number',
            'state_of_residence',
            'nationality',
            'profile_picture',
            'residential_address'
        ]
