from django.contrib import admin
from .models import Tutor, Subject, TutorReportAbuse, ProCourse

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    search_fields = ('id', 'first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('state_of_residence', 'nationality', 'email',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    search_fields = ('subject_name', 'id', 'subject_name', 'number_of_tutors',)
    list_filter = ('created_at', 'updated_at')

@admin.register(TutorReportAbuse)
class TutorReportAbuseAdmin(admin.ModelAdmin):
    list_display = ('id', 'target_client_id', 'message', 'subject')
    search_fields = ('id', 'target_client_id', 'subject',)
    list_filter = ('created_at',)

@admin.register(ProCourse)
class ProCourseAdmin(admin.ModelAdmin):
    search_fields = ('id', 'pro_course_name', 'number_of_tutors',)
    list_filter = ('created_at', 'updated_at')
