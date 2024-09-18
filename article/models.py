from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver

#! Métodos de seguridad 1
def custom_upload_to(instance, filename):
    if instance.pk:
        old_instance = Article.objects.get(pk=instance.pk)
        old_instance.image.delete()
    return 'article/' + filename

# Create your models here.
#! Artículos promocionales o simples blogs
class Article(models.Model):
    image = models.ImageField(upload_to=custom_upload_to, verbose_name="Imagen del artículo")
    title = models.CharField(max_length=100, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    user_post = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Quién lo publicó")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"

    def __str__(self):
        return self.title

  #! Métodos de seguridad 2
@receiver(post_delete, sender=Article)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False) 