from django.db import models

# Create your models here.


import uuid
from django.db import models
from django.utils.functional import cached_property


class Store(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    fiscal_identification = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=25, null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=255, null=True)


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    store = models.ForeignKey(Store, on_delete=models.RESTRICT)
    customer = models.CharField(max_length=255, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer_identification = models.CharField(max_length=25, null=True)
    card_number = models.CharField(max_length=25, null=True)

    def __str__(self):
        return f"{self.status} - {self.updated_at} - { self.amount}"

    @cached_property
    def status(self):
        return (
            self.payment_status.last().name
            if self.payment_status.last()
            else "No status"
        )

    class Meta:
        ordering = ["-updated_at"]
        db_table = "payment"
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos"


class PaymentStatus(models.Model):
    COMPLETED = "COMPLETED"
    CANCELED = "CANCELED"
    PAYMENT_STATUS = [
        (COMPLETED, "COMPLETED"),
        (CANCELED, "CANCELED"),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payment = models.ForeignKey(
        Payment, on_delete=models.CASCADE, related_name="payment_status"
    )
    name = models.CharField(max_length=10, choices=PAYMENT_STATUS, default=COMPLETED)
    description = models.CharField(max_length=255, null=True)
    meta_data = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.payment} - {self.name} "

    class Meta:
        ordering = ["created_at"]
        db_table = "payment_status"
        verbose_name = "Status do pagamento"
        verbose_name_plural = "Status dos pagamentos"
