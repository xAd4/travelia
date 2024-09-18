from django import forms
from destiny.models import Destiny
from location.models import Location

class PlaceFilterForm(forms.Form):
    #? Campo para seleccionar un destino (destiny)
    #? ModelChoiceField se usa para desplegar opciones basadas en los objetos de un modelo
    destiny = forms.ModelChoiceField(
        queryset=Destiny.objects.all(),  #? Este campo mostrará todas las instancias del modelo Destiny como opciones
        label="Destiny",  #? Etiqueta que se mostrará en el formulario
        widget=forms.Select(attrs={'class': 'form-control'})  #? Se utiliza el widget Select con una clase CSS 'form-control' para dar estilo
    )
    
    #? Campo para seleccionar una ubicación (location)
    location = forms.ModelChoiceField(
        queryset=Location.objects.all(),  #? Este campo mostrará todas las instancias del modelo Location como opciones
        label="Location",  #? Etiqueta que se mostrará en el formulario
        widget=forms.Select(attrs={'class': 'form-control'})  #? Se utiliza el widget Select con una clase CSS 'form-control' para dar estilo
    )
