from django.shortcuts import render
from tienda.models import Comic, Editorial, Reserva
from tienda.forms import FormReserva

def index(request):
    comics = Comic.objects.all()
    data = {'comics': comics}
    return render(request, 'index.html', data)

def reservar(request, id_comic):
    form = FormReserva()
    form.fields['id_comic'].initial = id_comic
    comic = Comic.objects.get(id=id_comic)
    data = {'form': form, 'comic': comic}
    return render(request, 'reservar.html', data)
