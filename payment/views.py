import logging
from django.shortcuts import render
from payment.models import Payment
from rest_framework import generics, status, filters
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from payment.permissions import IsPartner, IsDirector, IsAccountant
from payment.serializer import PaymentSerializer


logger = logging.getLogger(__name__)


class PaymentCreateView(generics.CreateAPIView):
    """
    Create a new payment
    """

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, IsPartner | IsDirector]

    def post(self, request, *args, **kwargs):
        logger.info(f"Request data: {request.data}")
        response = super().post(request, *args, **kwargs)
        logger.info(f"Response data: {response.data}")
        return response


class PaymentListView(generics.ListAPIView):
    """
    List all payments
    """

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["id", "amount", "status", "store", "created_at"]
    permission_classes = [IsAuthenticated, IsPartner | IsAccountant]

    def get(self, request, *args, **kwargs):
        logger.info(f"Request data: {request.data}")
        response = super().get(request, *args, **kwargs)
        logger.info(f"Response data: {response.data}")
        return response
