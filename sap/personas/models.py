from django.db import models

class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    numero = models.IntegerField()
    localidad = models.CharField(max_length=255)
    provincia = models.CharField(max_length=255)
    
    def __str__(self):
        return f"Domicilio {self.id}: {self.calle} {self.numero} | {self.localidad} - {self.provincia}"

class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    Domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"Persona {self.id}: {self.nombre} {self.apellido} | {self.email}"