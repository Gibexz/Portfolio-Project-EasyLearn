from django.contrib import admin
from lessonpedia.admin import lessonPedia_admin_site
from .models import Tutor, Subject,  ProCourse
# 

class TutorAdmin(admin.ModelAdmin):
    """Associates Tutor model to admin site"""
    list_display = ('id', 'username', 'first_name', 'email', 'created_at', 'updated_at')


class SubjectAdmin(admin.ModelAdmin):
    """Associates Subject model to admin site"""
    list_display = ('id', 'subject_name', 'tutor_count', 'related_subjects', 'created_at', 'updated_at')

admin.site.register(Tutor, TutorAdmin)
admin.site.register(Subject, SubjectAdmin)
# admin.site.register(TutorReportAbuse)
admin.site.register(ProCourse)


# registering other models in our lessonpedia site
lessonPedia_admin_site.register(Tutor, TutorAdmin)
lessonPedia_admin_site.register(Subject, SubjectAdmin)
# lessonPedia_admin_site.register(TutorReportAbuse)
lessonPedia_admin_site.register(ProCourse)