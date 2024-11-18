from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from Car.views import ExportView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("Car.urls")),
    path("export/<str:file_format>/", ExportView.as_view(), name="export"),

    path("api-token-auth/", views.obtain_auth_token),
]
