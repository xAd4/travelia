from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#! Promotional articles or simple blog
class Article(models.Model):
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

