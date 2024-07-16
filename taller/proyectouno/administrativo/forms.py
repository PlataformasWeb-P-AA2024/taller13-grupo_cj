from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Edificio, Departamento

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Ingrese nombre del edificio'),
            'direccion': _('Ingrese dirección'),
            'ciudad': _('Ingrese ciudad'),
            'tipo': _('Seleccione tipo de edificio'),
        }

    def clean_ciudad(self):
        valor = self.cleaned_data['ciudad']
        if valor.startswith('L'):
            raise forms.ValidationError("El nombre de la ciudad no puede iniciar con la letra mayúscula 'L'")
        return valor

    def clean_nombre(self):
        valor = self.cleaned_data['nombre']
        num_palabras = len(valor.split())
        if num_palabras < 2:
            raise forms.ValidationError("El nombre del edificio debe tener al menos 2 palabras")
        return valor

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['propietario', 'costo', 'numero_cuartos', 'edificio']
        labels = {
            'propietario': _('Ingrese nombre completo del propietario'),
            'costo': _('Ingrese el costo del departamento'),
            'numero_cuartos': _('Ingrese el número de cuartos'),
            'edificio': _('Seleccione el edificio'),
        }

    def clean_costo(self):
        valor = self.cleaned_data['costo']
        if valor > 100000:
            raise forms.ValidationError("El costo no puede ser mayor a $100 mil")
        return valor

    def clean_numero_cuartos(self):
        valor = self.cleaned_data['numero_cuartos']
        if valor == 0 or valor > 7:
            raise forms.ValidationError("El número de cuartos no puede ser 0 ni mayor a 7")
        return valor

    def clean_propietario(self):
        valor = self.cleaned_data['propietario']
        num_palabras = len(valor.split())
        if num_palabras < 3:
            raise forms.ValidationError("El nombre completo del propietario debe tener al menos 3 palabras")
        return valor
    
class DepartamentoEdificioForm(ModelForm):

    def __init__(self, edificio, *args, **kwargs):
        super(DepartamentoEdificioForm, self).__init__(*args, **kwargs)
        self.initial['edificio'] = edificio
        self.fields["edificio"].widget = forms.widgets.HiddenInput()
        print(edificio)

    class Meta:
        model = Departamento
        fields = ['propietario', 'costo', 'numero_cuartos', 'edificio']
        labels = {
            'propietario': _('Ingrese nombre completo del propietario'),
            'costo': _('Ingrese el costo del departamento'),
            'numero_cuartos': _('Ingrese el número de cuartos'),
            'edificio': _('Seleccione el edificio'),
        }

    def clean_costo(self):
        valor = self.cleaned_data['costo']
        if valor > 100000:
            raise forms.ValidationError("El costo no puede ser mayor a $100 mil")
        return valor

    def clean_numero_cuartos(self):
        valor = self.cleaned_data['numero_cuartos']
        if valor == 0 or valor > 7:
            raise forms.ValidationError("El número de cuartos no puede ser 0 ni mayor a 7")
        return valor