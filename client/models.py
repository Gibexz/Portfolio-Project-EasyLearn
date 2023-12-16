from django.db import models
from django.utils import timezone
from tutor.models import Tutor  # Import the Tutor model
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    username = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=15, null=True, unique=True)
    state_of_residence = models.CharField(max_length=50, null=True)
    nationality = models.CharField(max_length=50, null=True)
    profile_picture = models.CharField(max_length=200, unique=True)
    residential_address = models.CharField(max_length=150, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Changed to DateTimeField
    updated_at = models.DateTimeField(default=timezone.now, null=True)


class Review(models.Model):
    review_text = models.TextField(max_length=1000)
    tutor = models.ForeignKey(Tutor,  related_name='reviews', null=True, on_delete=models.SET_NULL)
    client = models.ForeignKey(Client, related_name='reviews', null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

class Ranking(models.Model):
    ranking_text = models.IntegerField(null=True)
    tutor = models.ForeignKey(Tutor, null=True, on_delete=models.SET_NULL, related_name='rankings')
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL, related_name='rankings')
    created_at = models.DateTimeField(auto_now_add=True)

class ClientReportAbuse(models.Model):
    target_tutor = models.ForeignKey(Tutor, related_name="reported_tutor", null=True, on_delete=models.SET_NULL)
    message = models.TextField(max_length=400)
    subject = models.CharField(max_length=100)
    client = models.ForeignKey(Client, related_name='abuse_reports', null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

class Cart(models.Model):
    target_tutor = models.ForeignKey(Tutor, related_name="selling_tutor", null=True, on_delete=models.SET_NULL)
    tutors_count = models.IntegerField(null=True)
    tutor_status = models.BooleanField(null=True)
    client = models.ForeignKey(Client,  related_name='carts', null=True, on_delete=models.SET_NULL)

class Payment(models.Model):
    tnx_id = models.CharField(null=True, max_length=200)
    time = models.DateTimeField(default=timezone.now)
    client = models.ForeignKey(Client, related_name='payments', null=True, on_delete=models.SET_NULL)

class PaymentReceipt(models.Model):
    receipt_id = models.CharField(null=True, max_length=200)
    payment_time = models.DateTimeField(default=timezone.now)
    client = models.ForeignKey(Client, related_name='payment_receipts', null=True, on_delete=models.SET_NULL)
