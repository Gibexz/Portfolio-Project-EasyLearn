from django.contrib import admin
from lessonpedia.admin import lessonPedia_admin_site
from .models import ClientReportAbuse, TutorReportAbuse

# Register your models here.
admin.site.register(ClientReportAbuse)
admin.site.register(TutorReportAbuse)


lessonPedia_admin_site.register(ClientReportAbuse)
lessonPedia_admin_site.register(TutorReportAbuse)