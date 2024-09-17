from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import post_delete
from django.dispatch import receiver
from destiny.models import Destiny
from location.models import Location


#! Method Security 1
def custom_upload_to(instance, filename):
    if instance.pk:
        old_instance = Place.objects.get(pk=instance.pk)
        old_instance.image.delete()
    return 'place/' + filename

# Create your models here.
#! Places to hang out
class Place(models.Model):
    image = models.ImageField(upload_to=custom_upload_to, verbose_name="Foto del lugar")
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
    
    def clean(self):
        if self.budget < 0:
            raise ValidationError({'budget': 'No puede ser negativo'})
    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

#! Method Security 2
@receiver(post_delete, sender=Place)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)