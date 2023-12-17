from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _

class LessonPediaAdminSite(AdminSite):
    site_header = _('LessonPedia Admin Panel')
    site_title = _('LessonPedia Admin Panel')

lessonPedia_admin_site = LessonPediaAdminSite(name='lessonpedia_admin')
