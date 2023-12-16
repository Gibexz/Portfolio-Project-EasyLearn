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


class Review(models.Model):
    "Tutor reviews by clients"
    reviewText = models.CharField(max_length=400)
    tutorID = models.IntegerField()


class Ranking(models.Model):
    "Tutor Rankings by clients"
    rankingText = models.IntegerField()
    tutorID = models.IntegerField()


class ClientReportAbuse(models.Model):
    "Client report abuse models"
    targetTutorID = models.IntegerField()
    message = models.CharField(max_length=400)
    subject = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)


class Cart(models.Model):
    "Client report abuse models"
    targetTutorID = models.IntegerField()
    tutorsCount = models.IntegerField(null=True)
    tutorStatus = models.BooleanField()


class Payment(models.Model):
    "Client Payment models"
    tnxID = models.CharField(null=True, max_length=200)
    time = models.DateField(timezone.now)


class Payment(models.Model):
    "Client Payment reciept models"
    receiptID = models.CharField(null=True, max_length=200)
    paymentTime = models.DateField(timezone.now)
