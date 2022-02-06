from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def home(request):
    
    datos = {}
    
    plantilla = loader.get_template('home.html')
    pagina = plantilla.render(datos,request)
        
    return HttpResponse(pagina)
