# Generated by Django 4.2.7 on 2023-12-17 15:22

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', models.CharField(max_length=15, null=True, unique=True)),
                ('gender', models.CharField(max_length=50, null=True)),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('highest_qualification', models.CharField(max_length=50, null=True)),
                ('employment_status', models.CharField(max_length=50, null=True)),
                ('state_of_residence', models.CharField(max_length=50, null=True)),
                ('nationality', models.CharField(max_length=50, null=True)),
                ('area_of_specialization', models.CharField(max_length=100, null=True)),
                ('personal_statement', models.TextField(max_length=5000, null=True)),
                ('availability', models.CharField(max_length=50, null=True)),
                ('working_hours', models.CharField(max_length=150, null=True)),
                ('status', models.BooleanField(null=True)),
                ('cv_id', models.IntegerField(null=True, unique=True)),
                ('profile_picture', models.ImageField(default='templates/lessonpedia/static/images/user/default_user_icon.png', upload_to='profile_picture/')),
                ('residential_address', models.CharField(max_length=255, null=True)),
                ('active_clients', models.IntegerField(default=0, null=True)),
                ('total_clients', models.IntegerField(default=0, null=True)),
                ('rejected_clients', models.IntegerField(default=0, null=True)),
                ('reviews_id', models.IntegerField(null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(related_name='tutor_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='tutor_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='TutorReportAbuse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_client_id', models.IntegerField()),
                ('message', models.TextField()),
                ('subject', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reported_client', to='tutor.tutor')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('tutor_count', models.IntegerField(null=True)),
                ('related_subjects', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tutors', models.ManyToManyField(related_name='subjects', to='tutor.tutor')),
            ],
        ),
        migrations.CreateModel(
            name='ProCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_course_name', models.CharField(max_length=100)),
                ('tutor_count', models.IntegerField(null=True)),
                ('related_pro_courses', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('tutors', models.ManyToManyField(related_name='pro_courses', to='tutor.tutor')),
            ],
        ),
    ]