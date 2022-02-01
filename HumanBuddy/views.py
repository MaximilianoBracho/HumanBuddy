from django.http import HttpResponse
from django.template import loader

def home(request):
    
    datos = {}
    
    plantilla = loader.get_template('home.html')
    pagina = plantilla.render(datos,request)
        
    return HttpResponse(pagina)