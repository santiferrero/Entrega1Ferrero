from django.db import models

# Create your models here.
class Artistas(models.Model):
    nombre= models.CharField(max_length=40)
    tipoArte= models.CharField(max_length=40)
    subTipoArte= models.CharField(max_length=30)


class Clientes(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Empleados(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    numeroEmpleado= models.IntegerField()
    email= models.EmailField()
    area= models.CharField(max_length=30)






