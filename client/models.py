from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Clients(models.Model):
    "Clients database"
    username = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=True)
    phoneNumber = models.CharField(max_length=15, null=True, unique=True)
    stateOfResidence = models.CharField(max_length=50, null=True)
    nationality = models.CharField(max_length=50, null=True)
    profilePicture = models.CharField(max_length=150, unique=True)
    residentialAddress = models.CharField(null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(default=timezone.now, null=True)