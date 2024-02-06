from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth.models import Group, Permission
from PIL import Image
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Tutor(AbstractUser):
    """Tutors database"""
    qualification_choice = [
        ('--select one--', '--select one--'),
        ('Phd', 'Phd'),
        ('Msc', "Msc"),
        ('BED', 'BED'),
        ('BSC', 'BSC'),
        ('BENG', 'BENG'),
        ('HND', 'HND'),
        ('OND', 'OND'),
        ('NCE', 'NCE'),
        ('SSCE', 'SSCE'),
        ('Others', 'Others')
    ]
    INSTITUTION_TYPES = [
        ('--select one--', '--select one--'),
        ('University', 'University'),
        ('Polytechnic', 'Polytechnic'),
        ('College Of Education', 'College Of Education'),
        ('Vocational', 'Vocational'),
        ('Others', 'Others'),
    ]

    RESULT = [
            ('--select one--', '--select one--'),
            ('First Class', 'First Class'),
            ('Distinction', 'Distinction'),
            ('Second Class Upper', 'Second Class Upper'),
            ('Upper credit', 'Upper credit'),
            ('Second Class Lower', 'Second Class Lower'),
            ('Lower credit', 'Lower credit'),
            ('Others', 'Others'),
            ]
    employment_type = [
        ('--select one--', '--select one--'),
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Freelance', 'Freelance'),
        ('Others', 'Others'),
    ]
    emp_status = [
            ('', '--select one--',),
            ('Employed', 'Employed'),
            ('Self Employed', 'Self Employed'),
            ('Unemployed', 'Unemployed'),
        ]
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    def generate_hour_choices():
        hours = []
        for hour in range(7, 23):
            time_str = f"{hour:02}:00"
            hours.append((time_str, time_str))
        return hours
    availability_choices = [
        ('', '--select one--'),
        ('Remote', 'Remote'),
        ('In-Person', 'In-Person'),
        ('Hybrid', 'Hybrid'),
    ]
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    open_to_work_choice = [
        ('', '--select one--'),
        ('Open', 'Open'),
        ('Not open to work', 'Not open to work'),
        ('Engaged', 'Engaged'),
    ]

    email = models.EmailField(max_length=150, unique=True)
    phone_number = models.CharField(max_length=15, null=True, unique=True)
    gender = models.CharField(max_length=50, default=timezone.now, null=True)
    marital_status = models.CharField(max_length=20, null=True)
    date_of_birth = models.DateField(null=True)
    institution = models.CharField(max_length=150, null=True)
    institution_type = models.CharField(max_length=20, choices=INSTITUTION_TYPES, default='--select one--', null=True)
    result = models.CharField(max_length=20, choices=RESULT, blank=True, null=True, default='--select one--')
    # quiz assessment
    quiz_result = models.FloatField(null=True, default=0.0)
    quiz_count = models.IntegerField(default=0, null=True)
    highest_qualification = models.CharField(max_length=50, choices=qualification_choice, default='--select one--', null=True)
    area_of_specialization = models.CharField(max_length=100, null=True)
    discipline = models.CharField(max_length=100, null=True)
    primary_subject = models.CharField(max_length=100, null=False)
    employment_type = models.CharField(max_length=50, choices=employment_type, null=True)
    employment_status = models.CharField(max_length=50, choices=emp_status, default='--select one--', null=True)
    lga_resident = models.CharField(max_length=50, null=True)
    state_of_residence = models.CharField(max_length=50, null=True)
    state_of_origin = models.CharField(max_length=50, null=True)
    nationality = models.CharField(max_length=50, null=True)
    bio = models.TextField(max_length=1000, null=True)
    status = models.CharField(max_length=50, null=True)
    availability = models.CharField(max_length=50, choices=availability_choices, null=True)
    average_session_duration = models.CharField(max_length=150, null=True)
    open_to_work = models.CharField(max_length=50, choices=open_to_work_choice, default='Open', blank=True)
    # suspend and block
    is_suspended = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    cv_id = models.FileField(upload_to='cv_files/', null=True, blank=True)
    highest_qualification_cert = models.FileField(upload_to='certs/highest_qualification/', null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_picture/', default='default_user_icon.png', validators=[FileExtensionValidator(allowed_extensions=['jpg','JPG', 'jpeg','JPEG', 'png', 'PNG'])])
    residential_address = models.CharField(max_length=255, null=True)
    reviews_id = models.IntegerField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    others = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    # work schedule
    average_class_duration = models.IntegerField(default=0, null=True)
    price_per_hour = models.IntegerField(default=500, null=True)
    negotiable = models.BooleanField(default=True, null=True)
    # tutor's client
    '''Contract model has a reverse relationship with Tutor and Client models with the name `contracts` '''
    active_contract_count = models.IntegerField(default=0, null=True)
    settled_contract_count = models.IntegerField(default=0, null=True)
    declined_contract_count = models.IntegerField(default=0, null=True)
    pending_contract_count = models.IntegerField(default=0, null=True)
    received_payment = models.IntegerField(default=0, null=True)
    total_contract_count = models.IntegerField(default=0, null=True)
    total_payment = models.IntegerField(default=0, null=True)
    cart_count = models.IntegerField(default=0, null=True)
    # rankings
    rank = models.FloatField(default=1.0, null=True)
    total_ratings = models.IntegerField(default=0)
    accumulated_rating = models.IntegerField(default=0)
    #
    groups = models.ManyToManyField(Group, related_name="tutor_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="tutor_permissions", blank=True)

    #suspension and ban(blocked) check
    is_suspended_admin = models.BooleanField(default=False)
    is_blocked_admin = models.BooleanField(default=False)
    suspended_at_admin = models.DateTimeField(null=True, blank=True)
    blocked_at_admin = models.DateTimeField(null=True, blank=True)
    suspension_duration_admin = models.IntegerField(default=0, null=True)
    suspension_reason_admin = models.TextField(null=True, blank=True)
    block_reason_admin = models.TextField(null=True, blank=True)


    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'profile_picture': self.profile_picture.url if self.profile_picture else None,
            'primary_subject': self.primary_subject,
            'subject': [subject.subject_name for subject in self.subjects.all()],
            'institution': self.institution,
            'rank': self.rank,
            'status': self.status,
        }

    def is_suspended_expired(self):
        if self.suspended_at_admin and self.suspension_duration_admin:
            return timezone.now() > self.suspended_at_admin + timezone.timedelta(days=self.suspension_duration_admin)
        return False


    def resize_image(self, image):

        img = Image.open(image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.profile_picture:
            self.resize_image(self.profile_picture)


    def __str__(self):
        return self.username


@receiver(post_delete, sender=Tutor)
def delete_subject_if_no_tutors(sender, instance, **kwargs):
    # Loop through the subjects associated with the deleted tutor
    for subject in instance.subjects.all():
        # If the subject has no other tutors, delete it
        if subject.tutors.count() == 0:
            subject.delete()

class PasswordResetToken(models.Model):
    user = models.OneToOneField(Tutor, on_delete=models.CASCADE)
    token = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        # Check if the token has expired (e.g., one-hour expiry)
        return (timezone.now() - self.created_at).total_seconds() > 3600

class Certificate(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='certificates')
    certificate_name = models.CharField(max_length=255)
    issuing_authority = models.CharField(max_length=255, null=True)
    date_of_issuance = models.DateField(null=True)
    certificate_file = models.FileField(upload_to='certs/other_certificate_files/')

    def __str__(self) -> str:
        return f"{self.tutor.username} - {self.certificate_name}"


class Hours(models.Model):
    name = models.CharField(max_length=10, choices=Tutor.generate_hour_choices(), unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Day(models.Model):
    name = models.CharField(max_length=10, choices=Tutor.DAY_CHOICES, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TimeSlot(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='schedules')
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    from_hour = models.ForeignKey(Hours, on_delete=models.CASCADE, related_name='from_hour')
    to_hour = models.ForeignKey(Hours, on_delete=models.CASCADE, related_name='to_hour')

    class Meta:
        unique_together = ('tutor', 'day', 'from_hour', 'to_hour')
        ordering = ['day__created_at', 'from_hour__created_at']
    def __str__(self):
        return f"{self.tutor.username}'s availability on {self.day} from {self.from_hour} to {self.to_hour}"

class SubjectCategory(models.Model):
    """ Tutors Subject Category Model"""
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    """Tutors Subject Model
    We will later consider putting these Choices in a separate model so that we can easily add more choices
    """
    CATEGORY_CHOICES = [
        ('Sciences', 'Sciences'),
        ('Art', 'Art'),
        ('Programming', 'Programming'),
        ('Mathematics', 'Mathematics'),
        ('Language Arts', 'Language Arts'),
        ('History', 'History'),
        ('Music', 'Music'),
        ('Cloud Computing', 'Cloud Computing'),
        ('Security', 'Security'),
        ('Data Science', 'Data Science'),
        ('Design', 'Design'),
        ('Artificial Intelligence', 'Artificial Intelligence'),
        ('Machine Learning', 'Machine Learning'),
        ('Law', 'Law'),
        ('Engineering', 'Engineering'),
        ('Medicine', 'Medicine'),
        ('Agriculture', 'Agriculture'),
        ('Architecture', 'Architecture'),
        ('Aviation', 'Aviation'),
        ('Communications', 'Communications'),
        ('Computer Science', 'Computer Science'),
        ('Economics', 'Economics'),
        ('Education', 'Education'),
        ('Environmental Science', 'Environmental Science'),
        ('Finance', 'Finance'),
        ('Geography', 'Geography'),
        ('Geology', 'Geology'),
        ('Journalism', 'Journalism'),
        ('Marketing', 'Marketing'),
        ('Physical Education', 'Physical Education'),
        ('Social Studies', 'Social Studies'),
        ('Business', 'Business'),
        ('Technology', 'Technology'),
        ('Foreign Language', 'Foreign Language'),
        ('Health', 'Health'),
        ('Philosophy', 'Philosophy'),
        ('Others', 'Others'),
    ]
    subject_name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(SubjectCategory, related_name='subjects', on_delete=models.CASCADE)
    proficiency = models.CharField(max_length=100, null=True)
    teaching_experience = models.CharField(max_length=100, null=True)
    tutor_count = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tutors = models.ManyToManyField(Tutor, related_name='subjects')

    @classmethod
    def update_tutor_count(cls):
        subjects = cls.objects.all()

        for subject in subjects:
            subject.tutor_count = subject.tutors.count()
            subject.save()


    def __str__(self):
        return self.subject_name

class ProCourse(models.Model):
    """Tutors ProCourses Model"""
    pro_course_name = models.CharField(max_length=100)
    tutor_count = models.IntegerField(null=True)
    related_pro_courses = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now, null=True)
    tutors = models.ManyToManyField(Tutor, related_name='pro_courses')

    def __str__(self):
        return self.pro_course_name