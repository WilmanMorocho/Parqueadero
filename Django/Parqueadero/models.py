from django.db import models

from statistics import mode
from tabnanny import verbose
from django.forms import IntegerField

class Auto(models.Model):
    placa=models.CharField(max_length=6)
    color=models.CharField(max_length=30)


    def __str__(self):
        return '{}'.format(self.placa)

class Propietario(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    cedula=models.CharField(max_length=10)
    idAuto=models.ForeignKey(Auto,on_delete=models.CASCADE)

    def __str__(self):
        return f'Nombre: {self.nombre}| Apellido:{self.apellido}| Cedula:{self.cedula}|Auto:{str(self.idAuto)}'

class Parqueo(models.Model):
    horaIngreso=models.CharField(max_length=5)
    horaSalida=models.CharField(max_length=5)
    idAuto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    idPropietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)

    def __str__(self):
        return f'Hora de Ingreso:{str(self.horaIngreso)}|Hora de Salida:{str(self.horaSalida)}|Auto:{self.idAuto}'
