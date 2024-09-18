from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

#! Method Security 1
def custom_upload_to(instance, filename):
    if instance.pk:
        old_instance = Work.objects.get(pk=instance.pk)
        old_instance.image.delete()
    return 'work/' + filename

# Create your models here.
#! Modelo de trabajo que indica las funciones de la empresa
class Work(models.Model):
    image = models.ImageField(upload_to=custom_upload_to, verbose_name="Imágen")
    title = models.CharField(max_length=100, verbose_name="Título")
    description = models.TextField(verbose_name="Contenido")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Trabajo"
        verbose_name_plural = "Nuestros trabajos"

    def __str__(self):
        return self.title

  #! Method Security 2
@receiver(post_delete, sender=Work)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)      