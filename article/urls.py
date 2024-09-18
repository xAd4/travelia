from django.urls import path
from . import views

#! Navegaciones
urlpatterns = [
    path("article/<int:pk>/", views.ArticleDetailView.as_view(), name="article-detail"),
]
