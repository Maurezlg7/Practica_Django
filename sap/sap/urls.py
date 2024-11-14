from django.contrib import admin
from django.urls import path
from personas.views import detallePersona, editarPersona, nuevaPersona, eliminarPersona
from webapp.views import bienvenido, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenido),
    path('home/', home, name='home'),
    path('detalle_persona/<int:id>/', detallePersona),
    path('nueva_persona/', nuevaPersona),
    path('editar_persona/<int:id>/', editarPersona),
    path('eliminar_persona/<int:id>/', eliminarPersona),
]
