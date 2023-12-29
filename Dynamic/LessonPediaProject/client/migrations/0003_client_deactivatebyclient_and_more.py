# Generated by Django 5.0 on 2023-12-29 07:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='deactivateByClient',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='profile_picture',
            field=models.ImageField(default='default_user_icon.png', upload_to='profile_picture/Client', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]),
        ),
    ]
