from django.contrib import admin

# Register your models here.

#!"Read Only Fields" Configuration
class ReadOnlyFields(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
