from re import template
from django import views
from django.shortcuts import render, get_object_or_404
from django.views import View
from menu.forms import PersonaForm, AnimalForm
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
    initial = {"nombre":"", "apellido": "",}

    def get(self, request):
      form = self.form_class(initial=self.initial)
      return render(request, self.template_name, {"form": form})

    def post(self, request):
      form = self.form_class(request.POST)

      if form.is_valid():
        form.save()
        form = self.form_class(initial=self.initial)
      return render(request, self.template_name, {"form":form})

class CargarAnimales(View):
    template_name = "menu/carga_de_animales.html"
    form_class = AnimalForm
    initial = {"Raza":"", "Alimentacion": "",}

    def get(self, request):
      form = self.form_class(initial=self.initial)
      return render(request, self.template_name, {"form": form})
    
    def post(self, request):
      form = self.form_class(request.POST)

      if form.is_valid():
        form.save()
        form = self.form_class(initial=self.initial)
      return render(request, self.template_name, {"form":form})

class ActualizarPersonas(View):
    template_name = "menu/actualizar_personas.html"
    success_template = "menu/exito.html"
    form_class = PersonaForm
    initial = {"nombre":"", "apellido": "", "fecha de nacimiento":""}

    def get(self, request, pk):
      persona = get_object_or_404(Persona, pk=pk)
      form = self.form_class(instance=persona)
      return render(request, self.template_name, {"form": form, "pk":pk})

    def post(self, request, pk):
      persona = get_object_or_404(Persona, pk=pk)
      form = self.form_class(request.POST, instance=persona)

      if form.is_valid():
        form.save()
        form = self.form_class(initial=self.initial)
      return render(request, self.success_template)


class ActualizarAnimales(View):
    template_name = "menu/actualizar_animales.html"
    success_template = "menu/exito.html"
    form_class = AnimalForm
    initial = {"Raza":"", "Alimentacion": "", "fecha de nacimiento":""}

    def get(self, request, pk):
      animal = get_object_or_404(Animal, pk=pk)
      form = self.form_class(instance=animal)
      return render(request, self.template_name, {"form": form, "pk":pk})
    
    def post(self, request, pk):
      animal = get_object_or_404(Animal, pk=pk)
      form = self.form_class(request.POST, instance=animal)

      if form.is_valid():
        form.save()
        form = self.form_class(initial=self.initial)
      return render(request, self.success_template)

