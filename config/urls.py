from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from tienda import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('reservar/<int:id_comic>/', views.reservar),
    path('comprobante/<int:id_reserva>/', views.comprobante),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
