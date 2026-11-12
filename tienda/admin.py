from django.contrib import admin
from .models import Editorial, Comic, Reserva

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Comic)
class ComicAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editorial', 'numero_tomo', 'tapa_dura', 'stock', 'precio', 'disponible')
    list_filter = ('editorial', 'tapa_dura', 'disponible')
    search_fields = ('titulo',)

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('comic', 'nombre_cliente', 'correo_cliente', 'rut_cliente', 'cantidad_ejemplares', 'fecha_y_hora_reserva', 'codigo_reserva')
    search_fields = ('nombre_cliente', 'correo_cliente', 'rut_cliente', 'codigo_reserva')