from django.forms import ModelForm
from django import forms

from ordenamiento.models import Barrio, Parroquia

class ParroquiaForm(ModelForm):
    class Meta:
        model = Parroquia
        fields = ['nombre', 'tipo']

class BarrioForm(ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombre','nroViviendas','nroParques', 'nroEdificios', 'parroquia']

class BarrioParroquiaForm(ModelForm):
    def __init__(self, parroquia, *args, **kwargs):
        super(BarrioParroquiaForm, self).__init__(*args, **kwargs)
        self.initial['parroquia'] = parroquia
        self.fields["parroquia"].widget = forms.widgets.HiddenInput()
        print(parroquia)

    class Meta:
        model = Barrio
        fields = ['nombre', 'nroViviendas', 'nroParques', 'nroEdificios', 'parroquia']