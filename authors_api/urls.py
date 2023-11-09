from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="FIFU API",
        default_version='v0.1',
        description='API endpoints',
        contact=openapi.Contact(email='pustovoitenkofilip@gmail.com'),
        license=openapi.License("MIT License")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('redoc/', schema_view.with_ui("redoc", cache_timeout=0)),
    path(settings.ADMIN_URL, admin.site.urls),
]

admin.site.site_header = 'FIFU api admin'
admin.site.site_title = "FIFU API Portal"
admin.site.index_title = "Welcome to FIFU API portal"
