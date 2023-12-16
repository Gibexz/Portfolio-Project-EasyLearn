from django.contrib import admin
from .models import AppAdmin

@admin.register(AppAdmin)
class AppAdminAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    search_fields = ('user__username', 'user__email')