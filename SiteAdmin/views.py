from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import redirect, render
from django.template import loader
from MyVet.models import Vet
from MyDaddy.models import Daddy
from SiteAdmin.forms import VetForm, DaddyForm

# Create your views here.

def manage(request):
    
    data = {}
    
    v_form = loader.get_template('SiteAdmin/manage.html')
    page = v_form.render(data,request)
      
    return HttpResponse(page)

def manageVets(request):
    
    vets = Vet.objects.all()
    v_context = {"vets":vets}          
            
    return render(request, 'SiteAdmin/manageVets.html',v_context)


def addVets(request):
    
    if(request.method == 'POST'):
        
        v_form = VetForm(request.POST)
        
        if v_form.is_valid():
            
            data = v_form.cleaned_data
            vet = Vet(
                fiscal_id=data["fiscal_id"],
                fiscal_name=data["fiscal_name"],
                name=data["name"],
                start_date=data["start_date"],
                fiscal_address=data["fiscal_address"],
                real_address=data["real_address"],
                phone=data["phone"],
                mail=data["mail"]
            )
            
            vet.save()
            
        return redirect('Gestión de Veterinarias')
            
    else:
            
        v_form = VetForm()
            
        return render(request, 'SiteAdmin/addVets.html',{"form": v_form})
    
def editVets(request,vetID):
    
    vet = Vet.objects.get(id=vetID)
        
    if(request.method == 'POST'):
        
        v_form = VetForm(request.POST, instance=vet)
        
        print(v_form)
        
        if v_form.is_valid():
            
            v_form.save()
            
        return redirect('Gestión de Veterinarias')
            
    else:
            
        v_form = VetForm(initial={
                "fiscal_id":vet.fiscal_id,
                "fiscal_name":vet.fiscal_name,
                "name":vet.name,
                "start_date":vet.start_date,
                "fiscal_address":vet.fiscal_address,
                "real_address":vet.real_address,
                "phone":vet.phone,
                "mail":vet.mail
            })
        
        return render(request, 'SiteAdmin/editVets.html',{"form": v_form, "id":vet.id})
    
def deleteVets(request, vetID):
    
    vet = Vet.objects.get(id=vetID)
    vet.delete()
    
    return redirect('Gestión de Veterinarias')

def manageDaddies(request):
    
    daddies = Daddy.objects.all()
    v_context = {"daddies":daddies}          
            
    return render(request, 'SiteAdmin/manageDaddies.html',v_context)


def addDaddies(request):
    
    if(request.method == 'POST'):
        
        v_form = DaddyForm(request.POST)
        
        if v_form.is_valid():
            
            data = v_form.cleaned_data
            daddy = Daddy(
                person_id=data["person_id"],
                name=data["name"],
                surname=data["surname"],
                birthdate=data["birthdate"],
                address=data["address"],
                phone=data["phone"],
                cellphone=data["cellphone"],
                mail=data["mail"],
                user_id=data["user_id"]
            )
            
            daddy.save()

        return redirect('Gestión de Padres')
            
    else:
            
        v_form = DaddyForm()
            
        return render(request, 'SiteAdmin/addDaddies.html',{"form": v_form})
    
def editDaddies(request,daddyID):
    
    daddy = Daddy.objects.get(id=daddyID)
        
    if(request.method == 'POST'):
        
        v_form = DaddyForm(request.POST, instance=daddy)
        
        print(v_form)
        
        if v_form.is_valid():
            
            v_form.save()
            
        return redirect('Gestión de Padres')
            
    else:
            
        v_form = DaddyForm(initial={
                "person_id":daddy.person_id,
                "name":daddy.name,
                "surname":daddy.surname,
                "birthdate":daddy.birthdate,
                "address":daddy.address,
                "phone":daddy.phone,
                "cellphone":daddy.cellphone,
                "mail":daddy.mail
            })
        
        return render(request, 'SiteAdmin/editDaddies.html',{"form": v_form, "id":daddy.id})
    
def deleteDaddies(request,daddyID):
    
    daddy = Daddy.objects.get(id=daddyID)
    daddy.delete()
    
    return redirect('Gestión de Padres')