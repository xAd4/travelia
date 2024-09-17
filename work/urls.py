from django.urls import path
from . import views

urlpatterns = [
    path("work/<int:pk>/", views.WorkDetailView.as_view(), name="work-detail"),
]
