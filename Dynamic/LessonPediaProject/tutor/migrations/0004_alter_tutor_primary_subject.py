# Generated by Django 5.0 on 2023-12-28 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0003_alter_tutor_primary_subject_alter_tutor_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='primary_subject',
            field=models.CharField(max_length=100),
        ),
    ]