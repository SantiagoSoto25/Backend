from django.db import models

class Personaje(models.Model):
    name = models.CharField(max_length=100)
    linea = models.CharField(max_length=100, default="-")
    movimiento = models.CharField(max_length=100, default="-")

    def str(self):
        return f'{self.id} - {self.name}'

class Arena(models.Model):
    name = models.CharField(max_length=100)
    modo = models.CharField(max_length=100)

    def str(self):
        return f'{self.id} - {self.name}'

class Skin(models.Model):
    name = models.CharField(max_length=100)
    coste = models.IntegerField()
    tipo = models.CharField(max_length=100)

    def str(self):
        return f'{self.id} - {self.name}'

class User(models.Model):
    name = models.CharField(max_length=128)
    personajes = models.ManyToManyField(Personaje, blank=True)
    arenas = models.ManyToManyField(Arena, blank=True)
    skins = models.ManyToManyField(Skin, blank=True)
    
    def str(self):
        return self.name
