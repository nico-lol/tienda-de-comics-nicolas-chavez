from django.shortcuts import render, redirect
from tienda.models import Comic, Editorial, Reserva
from tienda.forms import FormReserva
import datetime

def index(request):
    comics = Comic.objects.all()
    data = {'comics': comics}
    return render(request, 'index.html', data)

def comprobante(request, id_reserva):
    reserva = Reserva.objects.select_related('comic').get(id=id_reserva)
    valor_total = reserva.comic.precio * reserva.cantidad_ejemplares
    data = {'reserva': reserva, 'valor_total': valor_total}
    return render(request, 'comprobante.html', data)

def reservar(request, id_comic):
    form = FormReserva()
    form.fields['id_comic'].initial = id_comic

    if request.method == 'POST':
        form = FormReserva(request.POST)
        if form.is_valid():
            comic = Comic.objects.get(id = id_comic)
            cantidad_ejemplares = form.cleaned_data['cantidad_de_ejemplares']
            comic.stock -= cantidad_ejemplares
            comic.save()

            reserva = Reserva()
            reserva.comic = comic
            reserva.nombre_cliente = form.cleaned_data['nombre']
            reserva.correo_cliente = form.cleaned_data['correo']
            reserva.rut_cliente = form.cleaned_data['rut']
            reserva.cantidad_ejemplares = cantidad_ejemplares
            reserva.fecha_y_hora_reserva = datetime.datetime.now()
            reserva.codigo_reserva = form.cleaned_data['codigo']
            reserva.save()

            return redirect('/comprobante/' + str(reserva.id))



    comic = Comic.objects.get(id=id_comic)
    data = {'form': form, 'comic': comic}
    return render(request, 'reservar.html', data)
