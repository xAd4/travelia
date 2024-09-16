from django.contrib import admin
from helpers.admin import ReadOnlyFields
from .models import Place

# Register your models here.
admin.site.register(Place, ReadOnlyFields)
