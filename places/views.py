from django.views.generic import ListView
from .models import Place
from core.forms import PlaceFilterForm

class PlaceListView(ListView):
    model = Place
    template_name = 'places/place_list.html'
    context_object_name = 'places'

    def get_queryset(self):
        queryset = Place.objects.all()
        
        # Obtener los parámetros del formulario
        destiny = self.request.GET.get('destiny')
        location = self.request.GET.get('location')
        
        # Filtrar si se enviaron valores
        if destiny:
            queryset = queryset.filter(destiny_id=destiny)
        if location:
            queryset = queryset.filter(city_id=location)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pasamos el formulario al contexto para renderizarlo en la plantilla
        context['form'] = PlaceFilterForm(self.request.GET or None)
        return context
