from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth.models import Group, Permission

class Tutor(AbstractUser):
    """Tutors database"""
    qualification_choice = [
        ('--select one--', '--select one--'),
        ('Phd', 'Phd'),
        ('Msc', "Msc"),
        ('Bsc', 'Bsc'),
        ('Beng', 'Beng'),
        ('Hnd', 'Hnd'),
        ('ND', 'ND'),
        ('NCE', 'NCE'),
        ('Waec', 'Waec'),
        ('Others', 'Others')
    ]
    INSTITUTION_TYPES = [
        ('--select one--', '--select one--'),
        ('university', 'University'),
        ('polytechnic', 'Polytechnic'),
        ('COE', 'College Of Education'),
        ('vocational', 'Vocational'),
        ('others', 'Others'),
    ]

    RESULT = [
        ('--select one--', '--select one--'),
        ('first_class', 'First Class'),
        ('distinction', 'Distinction'),
        ('second_class_upper', 'Second Class Upper'),
        ('upper_credit', 'Upper Credit'),
        ('second_class_lower', 'Second Class Lower'),
        ('lower_credit', 'Lower Credit'),
        ('others', 'Others'),
    ]
    employment_type = [
        ('--select one--', '--select one--'),
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('freelance', 'Freelance'),
        ('others', 'Others'),
    ]
    emp_status = [
            ('', '--select one--',),
            ('Employed', 'Employed'),
            ('Self Employed', 'Self Employed'),
            ('Unemployed', 'Unemployed'),
        ]
    email = models.EmailField(max_length=150, unique=True)
    phone_number = models.CharField(max_length=15, null=True, unique=True)
    gender = models.CharField(max_length=50, default=timezone.now, null=True)
    date_of_birth = models.DateField(null=True)
    institution = models.CharField(max_length=150, null=True)
    institution_type = models.CharField(max_length=20, choices=INSTITUTION_TYPES, default='--select one--', null=True)
    result = models.CharField(max_length=20, choices=RESULT, blank=True, null=True, default='--select one--')
    highest_qualification = models.CharField(max_length=50, choices=qualification_choice, default='--select one--', null=True)
    area_of_specialization = models.CharField(max_length=100, null=True)
    discipline = models.CharField(max_length=100, null=True)
    employment_type = models.CharField(max_length=50, choices=employment_type, null=True)
    employment_status = models.CharField(max_length=50, choices=emp_status, default='--select one--', null=True)
    lga_resident = models.CharField(max_length=50, null=True)
    state_of_residence = models.CharField(max_length=50, null=True)
    nationality = models.CharField(max_length=50, null=True)
    personal_statement = models.TextField(max_length=5000, null=True)
    availability = models.CharField(max_length=50, null=True)
    working_hours = models.CharField(max_length=150, null=True)
    status = models.BooleanField(null=True)
    cv_id = models.FileField(upload_to='cv_files/', null=True, blank=True)
    certificate = models.FileField(upload_to='certificate_files/', null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_picture/', default='default_user_icon.png')
    residential_address = models.CharField(max_length=255, null=True)
    active_clients = models.IntegerField(default=0, null=True)
    total_clients = models.IntegerField(default=0, null=True)
    rejected_clients = models.IntegerField(default=0, null=True)
    reviews_id = models.IntegerField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    others = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 
    groups = models.ManyToManyField(Group, related_name="tutor_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="tutor_permissions", blank=True)

    def __str__(self):
        return self.username


class Subject(models.Model):
    """Tutors Subject Model"""
    CATEGORY_CHOICES = [
        ('sciences', 'Sciences'),
        ('programming', 'Programming'),
        ('mathematics', 'Mathematics'),
        ('language_arts', 'Language Arts'),
        ('history', 'History'),
        ('music', 'Music'),
        ('art', 'Art'),
        ('physical_education', 'Physical Education'),
        ('social_studies', 'Social Studies'),
        ('business', 'Business'),
        ('technology', 'Technology'),
        ('foreign_language', 'Foreign Language'),
        ('health', 'Health'),
        ('philosophy', 'Philosophy'),
        ('others', 'Others'),
    ]
    subject_name = models.CharField(max_length=100)
    category = models.CharField(max_length=25, choices=CATEGORY_CHOICES, null=True)
    tutor_count = models.IntegerField(null=True)
    related_subjects = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tutors = models.ManyToManyField(Tutor, related_name='subjects')


class TutorReportAbuse(models.Model):
    """Tutors report abuse models"""
    target_client_id = models.IntegerField()
    message = models.TextField()
    subject = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    tutor = models.ForeignKey(Tutor, related_name='reported_client', on_delete=models.CASCADE)


class ProCourse(models.Model):
    """Tutors ProCourses Model"""
    pro_course_name = models.CharField(max_length=100)
    tutor_count = models.IntegerField(null=True)
    related_pro_courses = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now, null=True)
    tutors = models.ManyToManyField(Tutor, related_name='pro_courses')