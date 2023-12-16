from django.contrib import admin
from .models import LessonPedia

@admin.register(LessonPedia)
class LessonPediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    search_fields = ('user__username', 'user__email')