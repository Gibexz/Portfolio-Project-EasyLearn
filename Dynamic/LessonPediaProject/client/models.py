from django.db import models
from django.utils import timezone
from django.db import models
from django.utils import timezone
from tutor.models import Tutor
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from django.core.validators import FileExtensionValidator


class Client (AbstractUser):
    deactivateByClient = models.BooleanField(default=True)
    email = models.EmailField(max_length=255, unique=True)
    others = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=15, null=True, unique=True)
    state_of_residence = models.CharField(max_length=50, null=True)
    nationality = models.CharField(max_length=50, null=True)
    profile_picture = models.ImageField(upload_to='profile_picture/Client', default='default_user_icon.png', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    residential_address = models.CharField(max_length=150, null=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    tutor = models.ManyToManyField(Tutor, related_name='engaged_tutor')
    date_of_birth = models.DateField(null=True)
    genderchoice = [
        ('Male', "Male"),
        ("Female", "Female")
        ]
    gender = models.CharField(max_length=10, choices=genderchoice, null=True)
    educational_level = models.CharField(max_length=200, null=True)
    # Added the below attributes to resolve permission and group conflict having same name
    # all inherits from Abstract user and hence need unique related_name
    groups = models.ManyToManyField(Group, related_name="client_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="client_permissions", blank=True)

        #suspension and ban(blocked) check
    is_suspended_admin = models.BooleanField(default=False)
    is_blocked_admin = models.BooleanField(default=False)
    suspended_at_admin = models.DateTimeField(null=True, blank=True)
    blocked_at_admin = models.DateTimeField(null=True, blank=True)
    suspension_duration_admin = models.IntegerField(default=0, null=True)
    suspension_reason_admin = models.TextField(null=True, blank=True)
    block_reason_admin = models.TextField(null=True, blank=True)

    def is_suspended_expired(self):
        if self.suspended_at_admin and self.suspension_duration_admin:
            return timezone.now() > self.suspended_at_admin + self.suspension_duration_admin #timezone.timedelta(days=self.suspension_duration)
        return False

class Review(models.Model):
    review_text = models.TextField(max_length=500)
    tutor = models.ForeignKey(Tutor,  related_name='reviews', null=True, on_delete=models.SET_NULL)
    client = models.ForeignKey(Client, related_name='reviews', null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

class Ranking(models.Model):
    rank_number = models.IntegerField(null=True)
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
    contract_validity = models.DateTimeField(null=True)
    contract_validated_start_date = models.DateTimeField(null=True)
    contract_validity_end_date = models.DateTimeField(null=True)
    client = models.ForeignKey(Client,  related_name='carts', null=True, on_delete=models.SET_NULL)

class Payment(models.Model):
    tnx_id = models.CharField(null=True, max_length=200)
    time = models.DateTimeField(default=timezone.now)
    client = models.ForeignKey(Client, related_name='payments', null=True, on_delete=models.SET_NULL)

class PaymentReceipt(models.Model):
    receipt_id = models.CharField(null=True, max_length=200)
    payment_time = models.DateTimeField(default=timezone.now)
    client = models.ForeignKey(Client, related_name='payment_receipts', null=True, on_delete=models.SET_NULL)
