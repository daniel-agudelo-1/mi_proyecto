from django.apps import AppConfig
from django.contrib import admin


class GestionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gestion'
    
def ready(self):
        admin.site.site_header = "Panel de Administración del Proyecto"
        admin.site.site_title = "Admin Proyecto"
        admin.site.index_title = "Gestor de Datos"
