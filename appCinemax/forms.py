from django import forms
from .models import Pelicula,Sala,Sesion,SalaSesion
#from django.forms import ModelForm, ClearableFileInput
class FormularioPelicula(forms.ModelForm):
    #nombreImagen  = forms.CharField(max_length=100)
    class Meta:
        model= Pelicula
        fields=["idPelicula","titulo","genero","clasificacion","director","interpretes",
                "sinopsis","imagenPortada","anio","duracion"]

class FormularioSala(forms.ModelForm):
    class Meta:
        model= Sala
        fields=["idSala","NumSala","NumAsientos","TipoDeSala"]

class FormularioSesion(forms.ModelForm):
    class Meta:
        model= Sesion
        fields=["idSesion","NumSesion","fecha","PrecioPorAsiento","AsientosLibres","AsientosVendidos"]

class FormularioSalaSesion(forms.ModelForm):
    class Meta:
        model= SalaSesion
        fields=["id_Sala","id_Sesion","idSalaSesion"]
