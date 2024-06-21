from django.urls import path
from lol import views

urlpatterns = [
    path('', views.personaje_list, name='personajes-list'),
    path('new_personaje', views.PersonajeCreateView.as_view(), name='PersonajeNuevo'),
    path('personajes_rest/', views.personajes_rest, name='personajes_rest'),
    path('users_restl/', views.users_restl, name='users_restl'),
    path('new_userl/', views.UserCreateView.as_view(), name='UserNuevo'),
    path('new_arena', views.ArenaCreateView.as_view(), name='ArenaNueva'),
    path('arena_rest/', views.arena_rest, name='arena_rest'),
    path('new_skin', views.SkinCreateView.as_view(), name='SkinNueva'),
    path('skin_rest/', views.skin_rest, name='skin_rest'),
]

