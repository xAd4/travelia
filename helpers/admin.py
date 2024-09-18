from django.contrib import admin

# Register your models here.

#!"Read Only Fields" Configuración
class ReadOnlyFields(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
