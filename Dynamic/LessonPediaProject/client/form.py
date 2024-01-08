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
            'residential_address',
            'date_of_birth',
            'gender',
            'educational_level',
            'prefered_channel',
            'prefered_language',
            'prefered_tutor_gender',
            'specific_educational_level',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'id': 'firstName', 'placeholder': 'First Name', 'required': 'required'}),
            'last_name': forms.TextInput(attrs={'id': 'lastName', 'placeholder': 'Last Name', 'required': 'required'}),
            'others': forms.TextInput(attrs={'id': 'others', 'placeholder': 'Other Names'}),
            'residential_address': forms.TextInput(attrs={'id': 'address', 'placeholder': 'Address', 'required': 'required'}),
            'state_of_residence': forms.TextInput(attrs={'id': 'state', 'placeholder': 'State of Resident', 'required': 'required'}),
            'educational_level': forms.Select(attrs={'id': 'eduLevel', 'required': 'required'}),
            'gender': forms.Select(attrs={'id': 'gender', 'required': 'required'}),
            'nationality': forms.TextInput(attrs={'id': 'nationality', 'placeholder': 'Nationality', 'required': 'required'}),
            'phone_number': forms.TextInput(attrs={'id': 'phoneNumber', 'placeholder': 'Phone Number', 'required': 'required'}),
            'profile_picture': forms.FileInput(attrs={'id': 'dp', 'class': 'file_button', 'type': 'file', 'required': 'required'}),
            'date_of_birth': forms.DateInput(attrs={'id': 'dob', 'placeholder': 'mm / dd / yyyy', 'required': 'required'}, format='%d-%m-%Y'),
            "specific_educational_level": forms.Select(attrs={'id': 'specifics'}),
            'prefered_channel': forms.Select(attrs={'id': 'channel', 'required': 'required'}),
            'prefered_language': forms.Select(attrs={'id': 'language', 'required': 'required'}),
            'prefered_tutor_gender': forms.Select(attrs={'id': 'tutorGender', 'required': 'required'}),
        }
        