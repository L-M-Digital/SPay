import logging
import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from payment.models import Payment, Store
from unittest import mock

logger = logging.getLogger(__name__)


@pytest.fixture
def authenticated_api_client():
    client = APIClient()
    user = User.objects.create_user(username="testuser", password="testpass")
    client.force_authenticate(user=user)
    return client


@pytest.fixture
def create_store():
    def _create_store(**kwargs):
        return Store.objects.create(**kwargs)

    return _create_store


@pytest.mark.django_db
def test_payment_create_view(authenticated_api_client, create_store):
    url = reverse("payment:payment-create")
    store = create_store(
        name="My Store",
        fiscal_identification="1234567890",
        phone="123-456-7890",
        email="test@email.com",
        address="123 Main St",
    )
    data = {
        "store": store.id,
        "customer": "John Doe",
        "amount": 100.00,
        "customer_identification": "1234567890",
        "card_number": "1234-5678-9012-3456",
    }

    response = authenticated_api_client.post(url, data, format="json")

    print(response.__dict__)

    assert response.status_code == status.HTTP_201_CREATED
    assert Payment.objects.count() == 1

    payment = Payment.objects.first()
    assert payment.customer == "John Doe"  # Adjust this based on your data
    # Add more assertions for other fields as needed


@pytest.mark.django_db
def test_payment_list_view(authenticated_api_client):
    url = reverse("payment:payment-list")

    response = authenticated_api_client.get(url)

    assert response.status_code == status.HTTP_200_OK

    # Add more assertions for verifying the list of payments and response data
