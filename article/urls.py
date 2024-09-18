from django.urls import path
from . import views

urlpatterns = [
    path("article/<int:pk>/", views.ArticleDetailView.as_view(), name="article-detail"),
]
