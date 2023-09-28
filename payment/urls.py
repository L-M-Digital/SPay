from django.urls import include, path
from payment.views import PaymentCreateView, PaymentListView

app_name = "payment"

urlpatterns = [
    path("create/", PaymentCreateView.as_view(), name="payment-create"),
    path("list/", PaymentListView.as_view(), name="payment-list"),
]
