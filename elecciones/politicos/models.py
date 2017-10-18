from django.db import models

# Create your models here.

class cargo():
    def __init__(self,desc):
        try:
            self.desc=str(desc)
        except Exception as e:
            raise e
        self.desc=desc

class politico():
    def __init__(self, nombre, apellido, email,cargo):
        try:
            self.nombre = str(nombre)
            self.apellido = str(apellido)
            self.email = str(email)
            self.cargo=cargo
        except Exception as e:
            raise e
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.cargo=cargo

class partido():

    def __init__(self,nombre):
        try:
            self.nombre=str(nombre)
            self.lista = []
        except Exception as e:
            raise e
        self.nombre=nombre
        self.lista = []

    def agregarPartido(self, partido):
        try:
            self.lista.append(partido)
        except Exception as e:
            raise e
        self.lista.append(partido)


