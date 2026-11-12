from django.contrib import admin
from .models import Editorial, Comic, Reserva
from django.utils.html import format_html

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Comic)
class ComicAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'portada_miniatura', 'editorial', 'numero_tomo', 'tapa_dura', 'stock', 'precio', 'disponible')
    list_filter = ('editorial', 'tapa_dura', 'disponible')
    search_fields = ('titulo',)
    readonly_fields = ('portada_miniatura',)

    @admin.display(description='Portada')
    def portada_miniatura(self, obj):
        if obj.portada:
            return format_html('<img src="{}" style="max-height: 150px;" />', obj.portada.url)
        return "-"

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('comic', 'nombre_cliente', 'correo_cliente', 'rut_cliente', 'cantidad_ejemplares', 'fecha_y_hora_reserva', 'codigo_reserva')
    search_fields = ('nombre_cliente', 'correo_cliente', 'rut_cliente', 'codigo_reserva')