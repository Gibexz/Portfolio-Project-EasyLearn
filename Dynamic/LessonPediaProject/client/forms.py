from django import forms
from .models import Client
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    phone_number = forms.CharField(max_length=15, required=False)
    state_of_residence = forms.CharField(max_length=50, required=False)
    nationality = forms.CharField(max_length=50, required=False)
    profile_picture = forms.ImageField(allow_empty_file=True, required=False)
    residential_address = forms.CharField(max_length=150, required=False)

    class Meta:
        model = Client
        fields =  (
                    'first_name', 'last_name', 'username', 'email', 
                    'phone_number', 'state_of_residence', 
                    'nationality', 'profile_picture', 
                    'residential_address', 'password1', 'password2',
                   )
