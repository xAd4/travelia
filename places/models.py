from django.db import models
from destiny.models import Destiny
from location.models import Location

# Create your models here.
#! Places to hang out
class Place(models.Model):
    name_place = models.CharField(max_length=100, verbose_name="Nombre del lugar")
    budget = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Presupuesto")
    destiny = models.ForeignKey(Destiny, on_delete=models.CASCADE, verbose_name="Tipo de lugar")
    city = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name="Ciudad")
    description = models.TextField(verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Lugar"
        verbose_name_plural = "Lugares"

    def __str__(self):
        return self.name_place
