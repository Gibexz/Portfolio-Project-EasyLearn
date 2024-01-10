from django.db import models
from django.utils import timezone
from client.models import Client
from tutor.models import  Tutor, Subject


class ContractManager(models.Manager):
    def active_contracts(self):
        return self.filter(contract_status='Active')
    

class Contract(models.Model):
    """Contract model"""
    CONTRACT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Active', 'Active'),
        ('Settled', 'Settled'),
        ('Declined', 'Declined'),
        ('Terminated', 'Terminated'),
    ]
    # WEEK_DAYS_CHOICES = [
    #     ('Mon', 'Mon'),
    #     ('Tue', 'Tue'),
    #     ('Wed', 'Wed'),
    #     ('Thu', 'Thu'),
    #     ('Fri', 'Fri'),
    #     ('Sat', 'Sat'),
    #     ('Sun', 'Sun'),
    # ]
    contract_code = models.CharField(max_length=10, unique=True)
    client = models.ForeignKey(Client, related_name='contracts', on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, related_name = 'contracts', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    pay_rate = models.DecimalField(max_digits=10, decimal_places=2)
    contract_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_made = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_remaining = models.DecimalField(max_digits=10, decimal_places=2)
    contract_length = models.IntegerField() # this is duration in days
    week_days = models.CharField(max_length=100, default='Mon')
    start_date = models.DateField()
    end_date = models.DateField()
    days_remaining = models.IntegerField()
    contract_status = models.CharField(max_length=20, choices=CONTRACT_STATUS_CHOICES, default='Pending')
    remark = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ContractManager()

    def __str__(self):
        return f"Contract #{self.pk} - {self.client} - {self.tutor} - {self.subject}"

    def save(self, *args, **kwargs):
        self.contract_amount = self.pay_rate * self.contract_length
        self.payment_remaining = max(self.contract_amount - self.payment_made, 0)
        self.days_remaining = max((self.end_date - timezone.now().date()).days, 0)
        if self.days_remaining == 0:
            self.contract_status = 'Settled'
        super().save(*args, **kwargs)



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

    def _str_(self):
        return self.subject
    
class ClientReportAbuse(models.Model):
    target_tutor = models.ForeignKey(Tutor, related_name="reported_tutor", null=True, on_delete=models.SET_NULL)
    message = models.TextField(max_length=1000)
    subject = models.CharField(max_length=100)
    client = models.ForeignKey(Client, related_name='abuse_reports', null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_by_admin = models.BooleanField(default=False, null=True)
    resolved_at = models.DateTimeField(null=True)