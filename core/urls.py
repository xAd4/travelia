from django.urls import path
from . import views

#! Navegaciones
urlpatterns = [
    path("", views.HomeTemplateView.as_view(), name="home"),
]
