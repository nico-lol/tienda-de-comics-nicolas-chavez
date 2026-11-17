from django.shortcuts import render, redirect
from tienda.models import Comic, Editorial, Reserva
from tienda.forms import FormReserva
import datetime
import secrets

def index(request):
    comics = Comic.objects.all()
    data = {'comics': comics}
    return render(request, 'index.html', data)

def formatear_rut(rut):
    rut_limpio = rut.replace('.', '').replace('-', '').strip().upper()
    if len(rut_limpio) < 2 or not rut_limpio[:-1].isdigit():
        return rut

    cuerpo = f'{int(rut_limpio[:-1]):,}'.replace(',', '.')
    return f'{cuerpo}-{rut_limpio[-1]}'

def comprobante(request, id_reserva):
    reserva = Reserva.objects.select_related('comic').get(id=id_reserva)
    valor_total = reserva.comic.precio * reserva.cantidad_ejemplares
    rut_formateado = formatear_rut(reserva.rut_cliente)
    data = {
        'reserva': reserva,
        'valor_total': valor_total,
        'rut_formateado': rut_formateado,
    }
    return render(request, 'comprobante.html', data)

def generar_codigo_reserva():
    while True:
        codigo = secrets.token_hex(5).upper()
        if not Reserva.objects.filter(codigo_reserva=codigo).exists():
            return codigo

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
            reserva.codigo_reserva = generar_codigo_reserva()
            reserva.save()

            return redirect('/comprobante/' + str(reserva.id))



    comic = Comic.objects.get(id=id_comic)
    data = {'form': form, 'comic': comic}
    return render(request, 'reservar.html', data)
