from django.contrib.auth.models import User
from django.db import models
from tutor.models import Tutor
from client.models import Client

class LessonPedia(models.Model):
    tutors = models.ManyToManyField(Tutor, related_name="clients", blank=True)
    clients = models.ManyToManyField(Client, related_name="tutors", blank=True)

