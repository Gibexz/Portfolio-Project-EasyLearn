from django.contrib import admin
from .models import AppAdmin
from lessonpedia.admin import lessonPedia_admin_site

class AppAdminAdmin(admin.ModelAdmin):
    """list view of admins"""
    list_display = ('id', 'username', 'email')


admin.site.register(AppAdmin, AppAdminAdmin)
lessonPedia_admin_site.register(AppAdmin, AppAdminAdmin)