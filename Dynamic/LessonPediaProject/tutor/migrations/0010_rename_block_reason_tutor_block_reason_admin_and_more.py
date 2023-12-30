# Generated by Django 5.0 on 2023-12-30 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0009_tutor_block_reason'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutor',
            old_name='block_reason',
            new_name='block_reason_admin',
        ),
        migrations.RenameField(
            model_name='tutor',
            old_name='blocked_at',
            new_name='blocked_at_admin',
        ),
        migrations.RenameField(
            model_name='tutor',
            old_name='is_blocked',
            new_name='is_blocked_admin',
        ),
        migrations.RenameField(
            model_name='tutor',
            old_name='is_suspended',
            new_name='is_suspended_admin',
        ),
        migrations.RenameField(
            model_name='tutor',
            old_name='suspended_at',
            new_name='suspended_at_admin',
        ),
        migrations.RenameField(
            model_name='tutor',
            old_name='suspension_duration',
            new_name='suspension_duration_admin',
        ),
        migrations.RenameField(
            model_name='tutor',
            old_name='suspension_reason',
            new_name='suspension_reason_admin',
        ),
    ]
