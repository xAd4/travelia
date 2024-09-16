from django.db import models

# Create your models here.
#! City where you will travel
class Location(models.Model):
    city = models.CharField(max_length=100, verbose_name="Nombre de la ciudad")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

    def __str__(self):
        return self.city