import pytest
from payment.models import Store


@pytest.fixture
def create_store():
    def _create_store(**kwargs):
        return Store.objects.create(**kwargs)

    return _create_store


@pytest.mark.django_db
def test_example_create_store(create_store):
    store_data = {
        "name": "My Store",
        "fiscal_identification": "1234567890",
        "phone": "123-456-7890",
        "email": "store@example.com",
        "address": "123 Main St",
    }

    store = create_store(**store_data)

    assert store.name == store_data["name"]
    assert store.fiscal_identification == store_data["fiscal_identification"]
    assert store.phone == store_data["phone"]
    assert store.email == store_data["email"]
    assert store.address == store_data["address"]
