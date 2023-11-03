from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static
from decorator_include import decorator_include

# from multifactor.decorators import multifactor_protected
import front_end.urls as front_end_urls


schema_view = get_schema_view(
    openapi.Info(
        title="Spay API",
        default_version="v1",
        description="Spay API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="luisgustavomarques@outlook.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # path("admin/multifactor/", include("multifactor.urls")),
    # path(
    #     "admin/", decorator_include(multifactor_protected(factors=1), admin.site.urls)
    # ),
    path("admin/", admin.site.urls),
    path("payment/", include("payment.urls")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    path("", include(front_end_urls)),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
