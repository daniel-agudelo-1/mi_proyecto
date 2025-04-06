from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('documento', 'nombres', 'apellidos', 'telefono', 'correo')
    search_fields = ('nombres', 'apellidos', 'documento')
    list_filter = ('nombres',)


admin.site.register(Cliente, ClienteAdmin)