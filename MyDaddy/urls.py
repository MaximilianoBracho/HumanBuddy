from django.urls import path
from MyDaddy import views

urlpatterns = [
    path('',views.manage, name="Portal de Padres"),
    path('add/',views.addDaddy, name="Alta de Padre"),
    path('profile/',views.manageDaddiesProfile, name="Gestión de Perfil"),
    path('pets/',views.managePets, name="Gestión de Mascotas"),
    path('pets/add/',views.addPets, name="Alta de Mascotas"),
    path('pets/edit/<petID>/',views.editPets, name="Editar Mascotas"),
    path('pets/delete/<petID>/',views.deletePets, name="Eliminar Mascotas")
]