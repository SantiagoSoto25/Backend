from rest_framework import serializers
from lol.models import Personaje, Arena, Skin

class PersonajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personaje
        fields = ['name', 'linea', 'movimiento', ]

class ArenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arena
        fields = ['name', 'modo' ]

class SkinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skin
        fields = ['name', 'coste', 'tipo' ]