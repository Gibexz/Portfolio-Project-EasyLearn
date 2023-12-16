from django.db import models

class AppAdmin(models.Model):
    username = models.CharField(max_length=100, unique=True, null=False)
    email =models.CharField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=100, null=False)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    profile_picture = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.username  # Display username in Django admin and shell
