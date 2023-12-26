from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class AppAdmin(AbstractUser):
    """Admin model for site administrators, developers and superusers"""
    email = models.EmailField(max_length=150, unique=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_picture = models.ImageField(upload_to='profile_picture/', default='default_user_icon.png')
    user_permissions = models.ManyToManyField(Permission, related_name='app_admin_permission', blank=True)
    groups = models.ManyToManyField(Group, related_name='app_admin_group', blank=True)

    def __str__(self):
        return self.username 

