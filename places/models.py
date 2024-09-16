from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#! Types of places, example: Restaurants, hotels and hospitals
class TypePlace(models.Model):
    type_place = models.CharField(max_length=100, verbose_name="Tipo de lugar")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Tipo de lugar"
        verbose_name_plural = "Tipo de lugares"

    def __str__(self):
        return self.type_place

#! Places to hang out
class Place(models.Model):
    name_place = models.CharField(max_length=100, verbose_name="Nombre del lugar")
    budget = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Presupuesto")
    type_place = models.ForeignKey(TypePlace, on_delete=models.CASCADE, verbose_name="Tipo de lugar")
    description = models.TextField(verbose_name="Descripción")
    user_post = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Quién lo publicó")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Lugar"
        verbose_name_plural = "Lugares"

    def __str__(self):
        return self.name_place
