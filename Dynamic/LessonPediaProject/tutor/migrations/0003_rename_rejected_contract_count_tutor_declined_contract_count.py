# Generated by Django 5.0 on 2024-01-05 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0002_remove_tutor_active_clients_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutor',
            old_name='rejected_contract_count',
            new_name='declined_contract_count',
        ),
    ]
