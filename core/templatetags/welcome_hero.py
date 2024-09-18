from django import template
from core.forms import PlaceFilterForm

register = template.Library()

@register.inclusion_tag("core/forms/welcome_hero.html", takes_context=True)
def welcome_form(context):
    #? Creamos una instancia del formulario PlaceFilterForm con los datos GET si los hay (request.GET)
    form = PlaceFilterForm(context['request'].GET or None)
    
    #? Retornamos un diccionario con el formulario para que sea usado dentro de la plantilla
    return {"form": form}
