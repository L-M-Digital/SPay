from django.contrib import admin
from django.http.request import HttpRequest
from payment.models import Payment, PaymentStatus, Store


class PaymentStatusInline(admin.TabularInline):
    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return False

    model = PaymentStatus
    extra = 0


class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "amount", "customer", "updated_at")
    search_fields = ("id", "customer", "customer_identification", "card_number")
    inlines = [PaymentStatusInline]


class StoreAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "fiscal_identification", "phone", "email", "address")
    search_fields = ("id", "name", "fiscal_identification", "phone", "email", "address")


admin.site.register(Payment, PaymentAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(PaymentStatus)
# Register your models here.
