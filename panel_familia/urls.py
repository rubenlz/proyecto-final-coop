from django.urls import path
from panel_familia.views import FamiliarList, FamiliarCrear,PersonaBorrar, PersonaActualizar

urlpatterns = [
    path('', FamiliarList.as_view(), name="persona-list"),
    path('crear', FamiliarCrear.as_view(), name="persona-crear"),
    path('<int:pk>/borrar', PersonaBorrar.as_view(), name="persona-borrar"),
    path('<int:pk>/actualizar', PersonaActualizar.as_view(),name="persona-actualizar"),

]