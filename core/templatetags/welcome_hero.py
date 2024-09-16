from django import template
from core.forms import PlaceFilterForm

register = template.Library()

@register.inclusion_tag("core/forms/welcome_hero.html", takes_context=True)
def welcome_form(context):
    form = PlaceFilterForm(context['request'].GET or None)
    return {"form": form}
