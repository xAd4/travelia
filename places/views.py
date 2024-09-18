from django.views.generic import ListView
from .models import Place
from core.forms import PlaceFilterForm

class PlaceListView(ListView):
    model = Place  
    template_name = 'places/place_list.html'  

    #? Método para obtener el queryset (lista de lugares) que se mostrará en la vista
    def get_queryset(self):
        #? Obtener todos los lugares sin filtro inicialmente
        queryset = Place.objects.all()
        
        #? Obtener los parámetros del formulario de filtro que vienen en la URL mediante GET
        destiny = self.request.GET.get('destiny')  #? Obtener el destino (restaurante, hotel, etc.)
        location = self.request.GET.get('location')  #? Obtener la ciudad
        
        #? Si se ha proporcionado un destino, filtrar los lugares por ese destino
        if destiny:
            queryset = queryset.filter(destiny_id=destiny)
        
        #? Si se ha proporcionado una ciudad, filtrar los lugares por esa ciudad
        if location:
            queryset = queryset.filter(city_id=location)
        
        #? Devolver el queryset filtrado o no, según lo ingresado por el usuario
        return queryset

    #? Método para agregar contexto adicional al template, como el formulario
    def get_context_data(self, **kwargs):
        #? Llamar al método padre para obtener el contexto base
        context = super().get_context_data(**kwargs)
        
        #? Agregar el formulario de filtro al contexto para que sea renderizado en la plantilla
        #? Si ya se han enviado datos mediante GET, los datos se mantendrán en el formulario
        context['form'] = PlaceFilterForm(self.request.GET or None)
        
        #? Retornar el contexto actualizado
        return context
