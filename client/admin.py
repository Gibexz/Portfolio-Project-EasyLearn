from django.contrib import admin
from .models import Client, Review, Ranking, ClientReportAbuse, Cart, Payment, PaymentReceipt
# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    ""
    search_fields = ('username', 'email', 'phone_number')
    list_filter = ('created_at', 'updated_at',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    ""
    search_fields = ('id', 'tutor', 'client',)
    list_filter = ('created_at',)


@admin.register(Ranking)
class RankingAdmin(admin.ModelAdmin):
    ""
    search_fields = ('id', 'tutor', 'client',)
    list_filter = ('created_at',)

@admin.register(ClientReportAbuse)
class ClientReportAbuseAdmin(admin.ModelAdmin):
    ""
    search_fields = ('id', 'target_tutor', 'client',)
    list_filter = ('created_at',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    search_fields = ('id', 'target_tutor', 'tutors_count', 'tutor_status', 'client',)
    list_filter = ('tutor_status',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    search_fields = ('tnx_id','time', 'client',)
    list_filter = ('time',)

@admin.register(PaymentReceipt)
class PaymentReceiptAdmin(admin.ModelAdmin):
    search_fields = ('receipt_id', 'id', 'receipt_id', 'payment_time', 'client',)
    list_filter = ('payment_time',)