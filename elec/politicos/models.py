from django.db import models

# Create your models here.


class cargo(models.Model):
    desc = models.CharField(max_length=500)

class partido(models.Model):
    nombre = models.CharField(max_length=50)
    nro_lista=models.IntegerField()

class politico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    partido= models.ForeignKey(partido)
    cargo=models.ForeignKey(cargo)