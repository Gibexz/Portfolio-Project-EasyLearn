# Generated by Django 5.0 on 2024-01-07 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_clientreportabuse_resolved_at_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ClientReportAbuse',
        ),
    ]
