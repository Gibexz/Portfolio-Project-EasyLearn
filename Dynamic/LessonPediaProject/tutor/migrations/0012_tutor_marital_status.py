# Generated by Django 5.0 on 2024-01-09 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0011_alter_subject_subject_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='marital_status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]