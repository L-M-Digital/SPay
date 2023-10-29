from django.contrib import admin
from django.http.request import HttpRequest
from payment.models import (
    Payment,
    PaymentStatus,
    Store,
    Partner,
    Director,
    Accountant,
)


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


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    )
    search_fields = (
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    )


admin.site.register(Payment, PaymentAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(PaymentStatus)
admin.site.register(Partner)
admin.site.register(Director)
admin.site.register(Accountant)
# Register your models here.
