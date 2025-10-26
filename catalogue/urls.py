from django.urls import path
from .views import index, ping

urlpatterns = [
    path("", index, name="catalogue_home"),   # /  (car inclus à la racine)
    path("ping/", ping, name="catalogue_ping"),
]
