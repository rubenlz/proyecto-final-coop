from socket import fromshare
from django.forms import froms
from menu.models import Persona, Animal

class PersonaForm(forms.ModelForm):
    class Meta:
      model = Persona
      fields = ['nombre', 'apellido', 'fecha_de_nacimiento']


class AnimalForm(forms.ModelForm):
    class Meta:
      model = Animal
      fields = ['raza', 'alimentacion', 'fecha_de_nacimiento']