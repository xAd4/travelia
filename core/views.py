from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import PlaceFilterForm

# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PlaceFilterForm()
        return context

    def post(self, request, *args, **kwargs):
        form = PlaceFilterForm(request.POST)
        if form.is_valid():
            # Procesar los datos si es necesario
            destiny = form.cleaned_data['destiny']
            location = form.cleaned_data['location']
            # Puedes hacer algo con destiny y location aquí

        return self.render_to_response(self.get_context_data(form=form))
