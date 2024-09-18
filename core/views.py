from django.views.generic import TemplateView
from .forms import PlaceFilterForm
from places.models import Place
from destiny.models import Destiny
from work.models import Work
from article.models import Article

# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PlaceFilterForm()

        restaurant = Destiny.objects.get(name_destiny="Restaurantes")
        context['places_restaurant'] = Place.objects.filter(destiny=restaurant).count()

        hotels = Destiny.objects.get(name_destiny="Hoteles")
        context['hotels'] = Place.objects.filter(destiny=hotels).count()

        healthcare = Destiny.objects.get(name_destiny="Hospitales")
        context['healthcare'] = Place.objects.filter(destiny=healthcare).count()

        context['works'] = Work.objects.all()

        context['articles'] = Article.objects.all()

        return context
    
    def post(self, request, *args, **kwargs):
        form = PlaceFilterForm(request.POST)
        if form.is_valid():
            destiny = form.cleaned_data['destiny']
            location = form.cleaned_data['location']

        return self.render_to_response(self.get_context_data(form=form))
