from django.db import models

# Create your models here.
#! Destino para el modelo "Place"
class Destiny(models.Model):
    name_destiny = models.CharField(max_length=100, verbose_name="Nombre del destino")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Destino"
        verbose_name_plural = "Destinos"

    def __str__(self):
        return self.name_destiny