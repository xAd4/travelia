from django.contrib import admin
from helpers.admin import ReadOnlyFields
from .models import Place

# Register your models here.
#! Registro de modelo
admin.site.register(Place, ReadOnlyFields)
