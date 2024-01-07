from django.db import models
from tutor.models import Tutor
from client.models import Client

# Create your models here.
class TutorReportAbuse(models.Model):
    """Tutors report abuse models"""
    target_client_id = models.ForeignKey(Client, related_name='reported_client', null=True, on_delete=models.SET_NULL)
    message = models.TextField(max_length=1000)
    subject = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    tutor = models.ForeignKey(Tutor, related_name='abuse_reports', on_delete=models.CASCADE)
    resolved_by_admin = models.BooleanField(default=False, null=True)
    resolved_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.subject
    
class ClientReportAbuse(models.Model):
    target_tutor = models.ForeignKey(Tutor, related_name="reported_tutor", null=True, on_delete=models.SET_NULL)
    message = models.TextField(max_length=1000)
    subject = models.CharField(max_length=100)
    client = models.ForeignKey(Client, related_name='abuse_reports', null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_by_admin = models.BooleanField(default=False, null=True)
    resolved_at = models.DateTimeField(null=True)