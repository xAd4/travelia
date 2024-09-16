from django import forms
from destiny.models import Destiny
from location.models import Location

class PlaceFilterForm(forms.Form):
    destiny = forms.ModelChoiceField(
        queryset=Destiny.objects.all(),
        label="Destiny",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    location = forms.ModelChoiceField(
        queryset=Location.objects.all(),
        label="Location",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
