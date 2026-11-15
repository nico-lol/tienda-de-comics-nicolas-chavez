from django.shortcuts import render
from tienda.models import Comic, Editorial, Reserva

def index(request):
    comics = Comic.objects.all()
    data = {'comics': comics}
    return render(request, 'index.html', data)
