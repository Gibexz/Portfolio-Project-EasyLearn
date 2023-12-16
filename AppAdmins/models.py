from django.db import models
from django.contrib.auth.models import User

class AppAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    username = models.CharField(max_length=100, unique=True, null=False)
    email =models.CharField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=100, null=False)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    profile_picture = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.username  # Display username in Django admin and shell
