# Generated by Django 5.0 on 2024-01-03 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_alter_ranking_rank_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientreportabuse',
            name='resolved_by_admin',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='review_subject',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
