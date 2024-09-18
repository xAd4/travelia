from django.views.generic import TemplateView
from .forms import PlaceFilterForm
from places.models import Place
from destiny.models import Destiny
from work.models import Work
from article.models import Article

# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'core/index.html'

    #? Este método se encarga de agregar datos al contexto que luego estarán disponibles en el template
    def get_context_data(self, **kwargs):
        #? Llamamos al método padre para obtener el contexto base
        context = super().get_context_data(**kwargs)
        
        #? Agregamos el formulario de filtro al contexto para que esté disponible en la plantilla
        context['form'] = PlaceFilterForm()

        #? Contamos cuántos lugares tienen como destino "Restaurantes"
        restaurant = Destiny.objects.get(name_destiny="Restaurantes")  #? Obtenemos el destino con nombre "Restaurantes"
        context['places_restaurant'] = Place.objects.filter(destiny=restaurant).count()  #? Contamos cuántos lugares están asociados con ese destino

        #? Contamos cuántos lugares tienen como destino "Hoteles"
        hotels = Destiny.objects.get(name_destiny="Hoteles")  #? Obtenemos el destino "Hoteles"
        context['hotels'] = Place.objects.filter(destiny=hotels).count()  #? Contamos cuántos lugares están asociados con "Hoteles"

        #? Contamos cuántos lugares tienen como destino "Hospitales"
        healthcare = Destiny.objects.get(name_destiny="Hospitales")  #? Obtenemos el destino "Hospitales"
        context['healthcare'] = Place.objects.filter(destiny=healthcare).count()  #? Contamos cuántos lugares están asociados con "Hospitales"

        #? Agregamos todos los trabajos al contexto para mostrarlos en el template
        context['works'] = Work.objects.all()

        #? Agregamos todos los artículos al contexto para mostrarlos en el template
        context['articles'] = Article.objects.all()

        #? Devolvemos el contexto actualizado
        return context
    
    #? Método para manejar solicitudes POST (cuando se envía el formulario)
    def post(self, request, *args, **kwargs):
        #? Cargamos el formulario con los datos enviados por el usuario
        form = PlaceFilterForm(request.POST)
        
        #? Verificamos si el formulario es válido
        if form.is_valid():
            #? Si es válido, obtenemos los valores de destino y ciudad desde el formulario
            destiny = form.cleaned_data['destiny']
            location = form.cleaned_data['location']

            #? Aquí podrías agregar lógica para procesar los datos o filtrar más información
        
        #? Renderizamos la respuesta con el contexto (incluyendo el formulario validado)
        return self.render_to_response(self.get_context_data(form=form))