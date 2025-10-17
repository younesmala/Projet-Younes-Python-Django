from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("catalogue/", include("catalogue.urls")),  # ← branche l'app ici
]
