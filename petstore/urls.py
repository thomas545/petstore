"""
petstore URL Configuration
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/", include("dj_rest_auth.registration.urls")),
    path("pets/", include("challenge_1.urls")),
]
