from re import template
from django import views
from django.shortcuts import render
from django.views import View

class ListarPersonas(View):
    template_name="menu/lista_de_personas.html"
    def get(self,request):
        return render(request,self.template_name)

class ListarAnimales(View):
    template_name="menu/lista_de_animales.html"
    def get(self,request):
        return render(request,self.template_name)

