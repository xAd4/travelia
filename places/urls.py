from django.urls import path
from .views import PlaceListView, PlaceDetailView

#! Navegaciones
urlpatterns = [
    path('places/', PlaceListView.as_view(), name='place_list'),
    path("places/<int:pk>/", PlaceDetailView.as_view(), name="place_detail")
]
