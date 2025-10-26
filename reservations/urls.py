from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("catalogue.urls")),        # la racine "/" va vers l'app
    path("admin/", admin.site.urls),
    # Option: garder aussi le préfixe /catalogue/ si tu veux
    # path("catalogue/", include("catalogue.urls")),
]
