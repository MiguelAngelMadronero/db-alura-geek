from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.CharField(max_length=200)
    img = models.URLField()
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre