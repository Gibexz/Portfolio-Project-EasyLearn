from django.contrib.auth.models import User
from django.db import models
from tutor.models import Tutor
from client.models import Client
from AppAdmins.models import AppAdmin

class LessonPedia(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    tutors = models.ManyToManyField(Tutor, related_name="clients", blank=True)
    clients = models.ManyToManyField(Client, related_name="tutors", blank=True)
    app_admin = models.ForeignKey(AppAdmin, related_name="app_administrator")

