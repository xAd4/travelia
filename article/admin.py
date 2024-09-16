from django.contrib import admin
from helpers.admin import ReadOnlyFields
from .models import Article

# Register your models here.
admin.site.register(Article, ReadOnlyFields)
