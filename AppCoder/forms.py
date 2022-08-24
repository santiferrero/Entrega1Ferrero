from socket import fromshare
from unittest.util import _MAX_LENGTH
from django import forms

class ArtistasFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    tipoArte= forms.CharField(max_length=30)
    subTipoArte= forms.CharField(max_length=30)

class ClientesFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()

class EmpleadosFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    numeroEmpleado= forms.IntegerField()
    email = forms.EmailField()
    area = forms.CharField(max_length=30)

