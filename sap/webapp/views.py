from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Persona


# Create your views here.
def bienvenido(request):
    return HttpResponse(f"Bienvenido a la aplicación de SAP")

def home(request):
    nro_personas = Persona.objects.count()
    #personas = Persona.objects.all()
    personas = Persona.objects.order_by('nombre', 'id') # descente -id
    #Si hay elementos repetidos, pasa a ordenarlos por el siguiente que se ingreso
    return render(request, "home.html", {'nro_personas':nro_personas, 'Personas':personas})