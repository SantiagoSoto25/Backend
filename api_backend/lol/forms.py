from django import forms
from lol.models import Personaje, User, Arena, Skin

class PersonajeForm(forms.ModelForm):
    class Meta:
        model = Personaje
        fields = ['name', 'linea', 'movimiento', ]

class ArenaForm(forms.ModelForm):
    class Meta:
        model = Arena
        fields = ['name', 'modo' ]

class SkinForm(forms.ModelForm):
    class Meta:
        model = Skin
        fields = ['name', 'coste', 'tipo' ]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'personajes', 'arenas', 'skins', ]

