from rest_framework import serializers
from rest_framework.pagination import LimitOffsetPagination
from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
