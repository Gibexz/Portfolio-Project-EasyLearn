
from django.contrib import admin
from lessonpedia.admin import lessonPedia_admin_site
from .models import Client, Cart, Ranking, Review, ClientReportAbuse, Payment, PaymentReceipt


class ClientAdmin(admin.ModelAdmin):
    """Associates Client model to admin site"""
    list_display = ('username', 'email', 'phone_number', 'state_of_residence', 'nationality', 'created_at')

admin.site.register(Client, ClientAdmin)
admin.site.register(Cart)
admin.site.register(Ranking)
admin.site.register(Review)
admin.site.register(ClientReportAbuse)
admin.site.register(Payment)
admin.site.register(PaymentReceipt)


lessonPedia_admin_site.register(Client, ClientAdmin)
lessonPedia_admin_site.register(Cart)
lessonPedia_admin_site.register(Ranking)
lessonPedia_admin_site.register(Review)
lessonPedia_admin_site.register(ClientReportAbuse)
lessonPedia_admin_site.register(Payment)
lessonPedia_admin_site.register(PaymentReceipt)
