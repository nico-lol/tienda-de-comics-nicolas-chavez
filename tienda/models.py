from django.db import models

class Editorial(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Comic(models.Model):
    titulo = models.CharField(max_length=50)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    portada = models.ImageField(upload_to='portadas/')
    numero_tomo = models.PositiveIntegerField()
    tapa_dura = models.BooleanField()
    stock = models.PositiveIntegerField()
    precio = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class Reserva(models.Model):
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    nombre_cliente = models.CharField(max_length=50)
    correo_cliente = models.EmailField()
    rut_cliente = models.CharField(max_length=10, unique=True)
    cantidad_ejemplares = models.PositiveIntegerField()
    fecha_y_hora_reserva = models.DateTimeField(auto_now_add=True)
    codigo_reserva = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"Reserva de {self.nombre_cliente} para {self.comic.titulo}"