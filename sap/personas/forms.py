from django.forms import EmailInput, ModelForm, TextInput
from personas.models import Persona, Domicilio

class Personaform(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type': 'email'}),
        }
        
class Direccionform(ModelForm):
    class Meta:
        model = Domicilio
        fields = '__all__'
        widgets = {
            'calle': TextInput(attrs={'type': 'email'}),
        }