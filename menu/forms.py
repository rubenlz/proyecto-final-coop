from socket import fromshare
from django import forms
from menu.models import Persona, Animal

class PersonaForm(forms.ModelForm):
    fecha_de_nacimiento = forms.DateField(label="Fecha de nacimiento", input_formats=[ "%d/%m/%Y" ],
    widget=forms.TextInput(attrs={'placeholder':'30/12/1988'}))

    class Meta:
      model = Persona
      fields = ['nombre', 'apellido', 'fecha_de_nacimiento']


class AnimalForm(forms.ModelForm):
    fecha_de_nacimiento = forms.DateField(label="Fecha de nacimiento", input_formats=[ "%d/%m/%Y" ],
    widget=forms.TextInput(attrs={'placeholder':'19/10/2020'}))
    class Meta:
      model = Animal
      fields = ['raza', 'alimentacion', 'fecha_de_nacimiento']