from django import forms
from tienda.models import Comic

class FormReserva(forms.Form):
    id_comic = forms.CharField(widget=forms.HiddenInput())
    nombre = forms.CharField()
    correo = forms.EmailField()
    rut = forms.CharField(max_length=9)
    cantidad_de_ejemplares = forms.IntegerField(min_value=1, max_value=3)
    codigo = forms.CharField()

    id_comic.widget.attrs.update({'class': 'form-control'})
    nombre.widget.attrs.update({'class': 'form-control'})
    correo.widget.attrs.update({'class': 'form-control'})
    rut.widget.attrs.update({'class': 'form-control'})
    cantidad_de_ejemplares.widget.attrs.update({'class': 'form-control'})
    codigo.widget.attrs.update({'class': 'form-control'})

    def clean_cantidad_de_ejemplares(self):
        id_comic = self.cleaned_data.get('id_comic')
        cantidad_de_ejemplares = self.cleaned_data['cantidad_de_ejemplares']

        if not id_comic:
            return cantidad_de_ejemplares

        comic = Comic.objects.filter(pk=id_comic).first()
        if comic is None:
            raise forms.ValidationError('El cómic seleccionado no existe.')

        if cantidad_de_ejemplares > comic.stock:
            raise forms.ValidationError(
                f'Solo hay {comic.stock} en el stock.'
            )

        return cantidad_de_ejemplares
        