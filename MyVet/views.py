from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from MyVet.models import Vet
from SiteAdmin.forms import VetForm

# Create your views here.

def manage(request):
    
    user=request.user
    
    vets = Vet.objects.filter(user_id=user.id)
    v_context = {"vets":vets}          
            
    return render(request, 'MyVet/manage.html',v_context)

def addVet(request):
    
    if(request.method == 'POST'):
        
        v_form = VetForm(request.POST)
        
        if v_form.is_valid():
            
            data = v_form.cleaned_data
            user=request.user
            
            vet = Vet(
                fiscal_id=data["fiscal_id"],
                fiscal_name=data["fiscal_name"],
                name=data["name"],
                start_date=data["start_date"],
                fiscal_address=data["fiscal_address"],
                real_address=data["real_address"],
                phone=data["phone"],
                mail=data["mail"],
                user_id=user.id
            )
            
            vet.save()
            
        return redirect('Gestión de Veterinaria')
            
    else:
            
        v_form = VetForm()
            
        return render(request, 'MyVet/addVet.html',{"form": v_form})
    
def editVet(request,vetID):
    
    vet = Vet.objects.get(id=vetID)
        
    if(request.method == 'POST'):
        
        v_form = VetForm(request.POST, instance=vet)
        
        print(v_form)
        
        if v_form.is_valid():
            
            v_form.save()
            
        return redirect('Gestión de Veterinaria')
            
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
        
        return render(request, 'MyVet/editVet.html',{"form": v_form, "id":vet.id})
    
def deleteVets(request, vetID):
    
    vet = Vet.objects.get(id=vetID)
    vet.delete()
    
    return redirect('Gestión de Veterinaria')