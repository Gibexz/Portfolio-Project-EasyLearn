# Generated by Django 5.0 on 2024-01-05 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generic_apps', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='contract_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Active', 'Active'), ('Completed', 'Completed'), ('Declined', 'Declined'), ('Terminated', 'Terminated')], default='Pending', max_length=20),
        ),
    ]