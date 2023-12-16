from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Tutors(models.Model):
    "Tutors database"
    firstName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=15, null=True, unique=True)
    gender = models.CharField(max_length=50, null=True)
    dateOfBirth = models.DateField(default=timezone.now())
    highestQualification = models.CharField(max_length=50, null=True)
    employementStatus = models.CharField(max_length=50, null=True)
    stateOfResidence = models.CharField(max_length=50, null=True)
    nationality = models.CharField(max_length=50, null=True)
    areaOfSpacialization = models.CharField(max_length=100, null=True)
    personalStatement = models.TextField(max_length=5000, null=True)
    avalability = models.CharField(max_length=50, null=True)
    workingHours = models.CharField(max_length=500, null=True)
    status = models.BooleanField(null=True)
    cvID = models.IntegerField(null=True, unique=True)
    profilePicture = models.CharField(max_length=150, unique=True)
    residentialAddress = models.CharField(null=True)
    activeClients = models.IntegerField(default=0, null=True)
    totalClients = models.IntegerField(default=0, null=True)
    rejectedClients = models.IntegerField(default=0, null=True)
    reviewsID = models.IntegerField(null=True, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(default=timezone.now, null=True)


class Subjects(models.Model):
    "Tutors Subject Model"
    subjectName = models.CharField(max_length=100)
    nunmberOfTutors = models.IntegerField(null=True)
    relatedSubjects = models.TextField(max, null=True)
    created_at= models.DateField(auto_now_add=True)
    updated_at = models.DateField(default=timezone.now(), null=True)


class TutorsReportAbuse(models.Model):
    "Tutors report abuse models"
    targetClientID = models.IntegerField()
    message = models.CharField(max_length=400)
    subject = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)


class ProCourses(models.Model):
    "Tutors ProCourses Model"
    ProCourseName = models.CharField(max_length=100)
    nunmberOfTutors = models.IntegerField(null=True)
    relatedProCourses = models.TextField(max, null=True)
    created_at= models.DateField(auto_now_add=True)
    updated_at = models.DateField(default=timezone.now(), null=True)
