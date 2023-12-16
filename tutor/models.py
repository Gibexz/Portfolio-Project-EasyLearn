from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone

class Tutor(models.Model):
    """Tutors database"""
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, null=True, unique=True)
    gender = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField(default=timezone.now)
    highest_qualification = models.CharField(max_length=50, null=True)
    employment_status = models.CharField(max_length=50, null=True)
    state_of_residence = models.CharField(max_length=50, null=True)
    nationality = models.CharField(max_length=50, null=True)
    area_of_specialization = models.CharField(max_length=100, null=True)
    personal_statement = models.TextField(max_length=5000, null=True)
    availability = models.CharField(max_length=50, null=True)
    working_hours = models.CharField(max_length=500, null=True)
    status = models.BooleanField(null=True)
    cv_id = models.IntegerField(null=True, unique=True)
    profile_picture = models.CharField(max_length=150, unique=True)
    residential_address = models.CharField(max_length=255, null=True)
    active_clients = models.IntegerField(default=0, null=True)
    total_clients = models.IntegerField(default=0, null=True)
    rejected_clients = models.IntegerField(default=0, null=True)
    reviews_id = models.IntegerField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now, null=True)


class Subject(models.Model):
    """Tutors Subject Model"""
    subject_name = models.CharField(max_length=100)
    number_of_tutors = models.IntegerField(null=True)
    related_subjects = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now, null=True)


class TutorReportAbuse(models.Model):
    """Tutors report abuse models"""
    target_client_id = models.IntegerField()
    message = models.CharField(max_length=400)
    subject = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class ProCourse(models.Model):
    """Tutors ProCourses Model"""
    pro_course_name = models.CharField(max_length=100)
    number_of_tutors = models.IntegerField(null=True)
    related_pro_courses = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now, null=True)
