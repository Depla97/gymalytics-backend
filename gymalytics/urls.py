from django.contrib import admin
from django.urls import path, include
from .views import schema_view

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("api/", include("gymsessionsapp.urls")),
    path("admin/", admin.site.urls),
]