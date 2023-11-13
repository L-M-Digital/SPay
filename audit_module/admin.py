from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseBase
from django.shortcuts import redirect
from django.template.response import TemplateResponse

# Register your models here.
from .models import Logs


class AdminLogs(admin.ModelAdmin):
    list_display = ("message", "timestamp")

    def change_view(
        self,
        request: HttpRequest,
        object_id: str,
        form_url: str = ...,
        extra_context: dict[str, bool] | None = ...,
    ) -> HttpResponse:
        return redirect("/admin/logs_page/")

    def changelist_view(
        self, request: HttpRequest, extra_context: dict[str, str] | None = ...
    ) -> TemplateResponse:
        return redirect("/admin/logs_page/", previous="/admin/")


admin.site.register(Logs, AdminLogs)
