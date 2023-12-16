from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone

class Client(models.Model):
    username = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=15, null=True, unique=True)
    state_of_residence = models.CharField(max_length=50, null=True)
    nationality = models.CharField(max_length=50, null=True)
    profile_picture = models.CharField(max_length=150, unique=True)
    residential_address = models.CharField(max_length=150, null=True)  # Added missing max_length
    created_at = models.DateTimeField(auto_now_add=True)  # Changed to DateTimeField
    updated_at = models.DateTimeField(default=timezone.now, null=True)

class Review(models.Model):
    review_text = models.CharField(max_length=400)
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming Tutor is a User model

class Ranking(models.Model):
    ranking_text = models.IntegerField()
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming Tutor is a User model

class ClientReportAbuse(models.Model):
    target_tutor = models.IntegerField()  # Change to ForeignKey if Tutor is a model
    message = models.CharField(max_length=400)
    subject = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)  # Changed to DateTimeField

class Cart(models.Model):
    target_tutor = models.IntegerField()  # Change to ForeignKey if Tutor is a model
    tutors_count = models.IntegerField(null=True)
    tutor_status = models.BooleanField()

class Payment(models.Model):
    tnx_id = models.CharField(null=True, max_length=200)
    time = models.DateTimeField(default=timezone.now)  # Changed to DateTimeField

class PaymentReceipt(models.Model):  # Changed model name to PaymentReceipt
    receipt_id = models.CharField(null=True, max_length=200)
    payment_time = models.DateTimeField(default=timezone.now)  # Changed to DateTimeField
