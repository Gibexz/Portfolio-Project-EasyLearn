# Generated by Django 5.0 on 2024-01-06 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generic_apps', '0005_alter_contract_contract_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='remark',
            field=models.TextField(blank=True),
        ),
    ]
