from django.contrib import admin
from lessonpedia.admin import lessonPedia_admin_site
from .models import Tutor, Subject, ProCourse, Day, TimeSlot, Hours, Certificate
from .models import SubjectCategory
from generic_apps.models import Contract
class TutorAdmin(admin.ModelAdmin):
    """Associates Tutor model to admin site"""
    list_display = ('id', 'username', 'first_name', 'email', 'created_at', 'updated_at')


class SubjectAdmin(admin.ModelAdmin):
    """Associates Subject model to admin site"""
    list_display = ('id', 'subject_name', 'tutor_count', 'created_at', 'updated_at')

admin.site.register(Tutor, TutorAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(ProCourse)
admin.site.register(Hours)
admin.site.register(Day)
admin.site.register(TimeSlot)
admin.site.register(Certificate)
admin.site.register(SubjectCategory)
admin.site.register(Contract)


# registering other models in our lessonpedia site
lessonPedia_admin_site.register(Tutor, TutorAdmin)
lessonPedia_admin_site.register(Subject, SubjectAdmin)
lessonPedia_admin_site.register(ProCourse)
lessonPedia_admin_site.register(Hours)
lessonPedia_admin_site.register(Day)
lessonPedia_admin_site.register(TimeSlot)
lessonPedia_admin_site.register(Certificate)
lessonPedia_admin_site.register(SubjectCategory)
lessonPedia_admin_site.register(Contract)