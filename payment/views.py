from django.shortcuts import render
from payment.models import Payment
from rest_framework import generics, status, filters
from rest_framework.views import APIView
from payment.serializer import PaymentSerializer


class PaymentCreateView(generics.CreateAPIView):
    """
    Create a new payment
    """

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentListView(generics.ListAPIView):
    """
    List all payments
    """

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["id", "amount", "status", "store", "created_at"]
