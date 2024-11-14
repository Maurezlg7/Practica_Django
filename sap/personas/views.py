from django.forms import modelform_factory
from django.shortcuts import get_object_or_404, redirect, render

from personas.models import Persona
from personas.forms import Personaform

# Create your views here.
def detallePersona(request, id):
    #persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    return render(request, "personas/detalle.html", {'persona': persona})

#Personaform = modelform_factory(Persona, exclude=[])


def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = Personaform(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('home')
        else:
            print(f"{formaPersona.errors}")
    else:
        formaPersona = Personaform()
        return render(request, "personas/nuevo.html", {'formaPersona': formaPersona})
    
def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        formaPersona = Personaform(request.POST, instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('home')
        else:
            print(f"{formaPersona.errors}")
    else:
        formaPersona = Personaform(instance=persona)
        return render(request, "personas/editar.html", {'formaPersona': formaPersona})
    
def eliminarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    
    return redirect('home')