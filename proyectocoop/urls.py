"""proyectocoop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from menu.views import ListarPersonas, ListarAnimales, CargarPersonas, CargarAnimales, ActualizarPersonas, ActualizarAnimales

urlpatterns = [
    path('admin/', admin.site.urls),
    path('personas/', ListarPersonas.as_view()),
    path('animales/', ListarAnimales.as_view()),
    path('personas/cargar', CargarPersonas.as_view()),
    path('animales/cargar', CargarAnimales.as_view()),
    path('personas/actualizar', ActualizarPersonas.as_view()),
    path('personas/actualizar/<int:pk>', ActualizarPersonas.as_view()),
    path('animales/actualizar', ActualizarAnimales.as_view()),
    path('animales/actualizar/<int:pk>', ActualizarAnimales.as_view()),
]