# Generated by Django 4.1.3 on 2024-09-17 21:40

from django.db import migrations, models
import work.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=work.models.custom_upload_to, verbose_name='Imágen')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Contenido')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Trabajo',
                'verbose_name_plural': 'Nuestros trabajos',
            },
        ),
    ]