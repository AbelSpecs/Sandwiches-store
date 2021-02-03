from django import forms
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class FechaForm(forms.Form):
    fecha = forms.DateTimeField(widget=DateInput())
    
class SandwichForm(forms.Form):
    tamaño = forms.CharField(max_length=100)
    
class CLienteForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    
class IngredienteForm(forms.Form):
    ingrediente = forms.CharField(max_length=100)