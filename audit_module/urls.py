from django.urls import path
from audit_module.views import LogsAuditView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", login_required(LogsAuditView.as_view()), name="logs_view"),
]
