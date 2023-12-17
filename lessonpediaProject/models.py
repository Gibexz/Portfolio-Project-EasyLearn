from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from tutor.models import Tutor
from client.models import Client
# from AppAdmins.models import AppAdmin

class LessonPedia(AbstractUser):
    tutors = models.ManyToManyField(Tutor, related_name="clients", blank=True)
    clients = models.ManyToManyField(Client, related_name="tutors", blank=True)
    groups = models.ManyToManyField(Group, related_name='lessonpedia_group')
    user_perimissions = models.ManyToManyField(Permission, related_name='lessonpedia_permission')
    # app_admin = models.ForeignKey(AppAdmin, related_name="app_administrator", on_delete=models.CASCADE)
