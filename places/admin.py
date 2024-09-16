from django.contrib import admin
from helpers.admin import ReadOnlyFields
from .models import TypePlace, Place

# Register your models here.
admin.site.register(TypePlace, ReadOnlyFields)
admin.site.register(Place, ReadOnlyFields)
