# Generated by Django 5.0 on 2024-01-08 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0010_alter_tutor_price_per_hour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]