from django.contrib import admin
from .models import Artist  # on importe le modèle Artist

# On enregistre le modèle Artist dans l'interface d'admin
admin.site.register(Artist)
