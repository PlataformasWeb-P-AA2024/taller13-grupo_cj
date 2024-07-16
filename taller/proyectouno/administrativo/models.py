from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Edificio(models.Model):
    TIPO_CHOICES = [
        ('residencial', 'Residencial'),
        ('comercial', 'Comercial'),
    ]
    
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    tipo = models.CharField(max_length=12, choices=TIPO_CHOICES)

    def __str__(self):
        return "%s - %s - %s - %s" %(
            self.nombre,
            self.direccion,
            self.ciudad,
            self.tipo
        )

class Departamento(models.Model):
    propietario = models.CharField(max_length=255)
    costo = models.IntegerField()
    numero_cuartos = models.IntegerField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE)

    def _str_(self):
        return "%s - %d - %d" % (
            self.propietario,
            self.costo,
            self.numero_cuartos,
        )
    
    