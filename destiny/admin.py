from django.contrib import admin
from helpers.admin import ReadOnlyFields
from .models import Destiny

# Register your models here.
admin.site.register(Destiny, ReadOnlyFields)