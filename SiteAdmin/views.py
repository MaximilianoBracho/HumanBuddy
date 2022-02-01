from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

# Create your views here.

def manage(request):
    
    datos = {}
    
    plantilla = loader.get_template('SiteAdmin/manage.html')
    pagina = plantilla.render(datos,request)
      
    return HttpResponse(pagina)

# Create your views here.
