from django import forms
from tienda.models import Reserva

class FormReserva(forms.Form):
    id_comic = forms.CharField(widget=forms.HiddenInput())
    nombre = forms.CharField()
    correo = forms.EmailField()
    rut = forms.CharField()
    cantidad_de_ejemplares = forms.IntegerField()
    codigo = forms.CharField()

    id_comic.widget.attrs.update({'class': 'form-control'})
    nombre.widget.attrs.update({'class': 'form-control'})
    correo.widget.attrs.update({'class': 'form-control'})
    rut.widget.attrs.update({'class': 'form-control'})
    cantidad_de_ejemplares.widget.attrs.update({'class': 'form-control'})
    codigo.widget.attrs.update({'class': 'form-control'})