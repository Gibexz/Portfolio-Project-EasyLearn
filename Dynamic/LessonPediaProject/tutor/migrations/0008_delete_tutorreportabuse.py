# Generated by Django 5.0 on 2024-01-06 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0007_tutor_cart_count'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TutorReportAbuse',
        ),
    ]