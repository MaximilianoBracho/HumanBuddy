from django.urls import path
from MyVet import views

urlpatterns = [
    path('',views.manage, name="Gestión de Veterinaria"),
    path('add/',views.addVet, name="Alta de Veterinaria"),
]