from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['documento', 'nombres', 'apellidos', 'telefono', 'correo', 'direccion']