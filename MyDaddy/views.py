from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from MyDaddy.models import Pet, Daddy
from MyDaddy.forms import DaddyForm, PetForm

def manage(request):
    
    datos = {}
    
    plantilla = loader.get_template('MyDaddy/manage.html')
    pagina = plantilla.render(datos,request)
      
    return HttpResponse(pagina)

def addDaddy(request):

    user=request.user
    if not Daddy.objects.filter(user_id=user.id).exists():
    
        if(request.method == 'POST'):
            
            v_form = DaddyForm(request.POST)
            
            if v_form.is_valid():
                
                user = request.user
                
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
                    user_id=user.id,
                )
                
                daddy.save()

            return redirect('Portal de Padres')
            
        else:
            
            v_form = DaddyForm()
                
            return render(request, 'MyDaddy/addDaddySignup.html',{"form": v_form})
    else:
        
        return redirect('Portal de Padres')

def editDaddyProfile(request):
    
    user=request.user
    daddy=Daddy.objects.get(user_id=user.id)
        
    if(request.method == 'POST'):
        
        v_form = DaddyForm(request.POST, instance=daddy)
        
        print(v_form)
        
        if v_form.is_valid():
            
            v_form.save()
            
        return redirect('Portal de Padres')
            
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
        
        return render(request, 'MyDaddy/editProfile.html',{"form": v_form, "id":daddy.id})

def managePets(request):
    
    user=request.user
    daddy=Daddy.objects.get(user_id=user.id)
    
    pets = Pet.objects.filter(daddy_id=daddy.id)
    v_context = {"pets":pets}          
            
    return render(request, 'MyDaddy/managePets.html',v_context)

def addPets(request):
    
    if(request.method == 'POST'):
        
        v_form = PetForm(request.POST)
        
        if v_form.is_valid():
            
            user=request.user
            daddy=Daddy.objects.get(user_id=user.id)
            
            data = v_form.cleaned_data
            
            pet = Pet(
                species=data["species"],
                family=data["family"],
                race=data["race"],
                color=data["color"],
                nickname=data["nickname"],
                birthdate=data["birthdate"],
                vet_id=data["vet_id"],
                daddy_id=daddy.id
            )
            
            pet.save()
            
        return redirect('Gestión de Mascotas')
            
    else:
            
        v_form = PetForm()
            
        return render(request, 'MyDaddy/addPets.html',{"form": v_form})
                        
def editPets(request,petID):
    
    pet = Pet.objects.get(id=petID)
        
    if(request.method == 'POST'):
        
        v_form = PetForm(request.POST, instance=pet)
        
        print(v_form)
        
        if v_form.is_valid():
            
            v_form.save()
            
        return redirect('Gestión de Mascotas')
            
    else:
            
        v_form = PetForm(initial={
                "species":pet.species,
                "family":pet.family,
                "race":pet.race,
                "color":pet.color,
                "nickname":pet.nickname,
                "birthdate":pet.birthdate,
                "vet_id":pet.vet_id
            })
        
        return render(request, 'MyDaddy/editPets.html',{"form": v_form, "id":pet.id})                  

def deletePets(request,petID):
    
    pet = Pet.objects.get(id=petID)
    pet.delete()
    
    return redirect('Gestión de Mascotas')
                        