from re import template
from django import views
from django.shortcuts import render
from django.views import View

from menu.models import Animal, Persona

class ListarPersonas(View):
    template_name="menu/lista_de_personas.html"
    def get(self,request):
      personas =Persona.objects.all()
      return render(request,self.template_name, {"persona": personas})

class ListarAnimales(View):
    template_name="menu/lista_de_animales.html"
    def get(self,request):
      animales = Animal.objects.all()
      return render(request,self.template_name, {"animal": animales})


class CargarPersonas(View):
    template_name = "menu/carga_de_personas.html"
    form_class = PersonaForm