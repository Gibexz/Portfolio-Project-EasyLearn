# Generated by Django 5.0 on 2023-12-30 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_client_deactivatebyclient_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='block_reason_admin',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='blocked_at_admin',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='is_blocked_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='client',
            name='is_suspended_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='client',
            name='suspended_at_admin',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='suspension_duration_admin',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='suspension_reason_admin',
            field=models.TextField(blank=True, null=True),
        ),
    ]