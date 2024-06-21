from lol.models import Personaje, Arena, Skin
from django.views.generic.edit import CreateView
from lol.forms import PersonajeForm, UserForm, ArenaForm, SkinForm
from lol.serializers import PersonajeSerializer, ArenaSerializer, SkinSerializer
from django.shortcuts import render 
from django.http import JsonResponse

class PersonajeCreateView(CreateView):
    form_class = PersonajeForm
    template_name = 'personaje_form.html'  
    success_url = '/'  

class ArenaCreateView(CreateView):
    form_class = ArenaForm
    template_name = 'arena_form.html'  
    success_url = '/' 

class SkinCreateView(CreateView):
    form_class = SkinForm
    template_name = 'skin_form.html'  
    success_url = '/' 

class UserCreateView(CreateView):
    form_class = UserForm
    template_name = 'user_form.html'  
    success_url = '/'  

def get_all_personajes():
    personajes = Personaje.objects.all().order_by('name')
    personajes_serializers = PersonajeSerializer(personajes, many=True)
    return personajes_serializers.data

def get_all_arenas():
    arenas = Arena.objects.all().order_by('name')
    arenas_serializers = ArenaSerializer(arenas, many=True)
    return arenas_serializers.data

def get_all_skins():
    skins = Skin.objects.all().order_by('coste')
    skins_serializers = SkinSerializer(skins, many=True)
    return skins_serializers.data

def personaje_list(request):
    personajes = get_all_personajes()
    arenas = get_all_arenas()
    skins = get_all_skins()
    return render(request, 'personaje_list.html', {'personajes': personajes, 'arenas': arenas, 'skins': skins})

def personajes_rest(request):
    personajes = get_all_personajes()
    return JsonResponse(personajes, safe=False)

def arena_rest(request):
    arenas = get_all_arenas()
    return JsonResponse(arenas, safe=False)

def skin_rest(request):
    skins = get_all_skins()
    return JsonResponse(skins, safe=False)

def users_restl(request):
    return JsonResponse("Ok", safe=False)

