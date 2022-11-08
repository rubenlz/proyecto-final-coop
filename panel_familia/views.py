from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from menu.models import Persona

class FamiliarList(ListView):
  model = Persona


class FamiliarCrear(CreateView):
  model = Persona
  success_url = "/panel-familia"
  fields = ["nombre", "apellido"]

class PersonaBorrar(DeleteView):
  model = Persona
  success_url = "/panel-familia"

class PersonaActualizar(UpdateView):
  model = Persona 
  success_url = "/panel-familia"
  fields = ["nombre", "apellido"]
