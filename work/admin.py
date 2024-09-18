from django.contrib import admin
from helpers.admin import ReadOnlyFields
from .models import Work

# Register your models here.

#!"Read Only Fields" Configuration
class ReadOnlyFields(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

#! Registro de modelo
admin.site.register(Work, ReadOnlyFields)
