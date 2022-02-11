from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from MyCare.models import CareAttention, Message
from MyCare.forms import CareForm, MessageForm
from MyVet.models import Veterinarian
from MyDaddy.models import Pet, Daddy

# Create your views here.

def manage(request):
    
    user=request.user
    veterinarian=Veterinarian.objects.get(user_id=user.id)
    
    pets = Pet.objects.filter(vet_id=veterinarian.vet_id)
    v_context = {"pets":pets}          
            
    return render(request, 'MyCare/manage.html',v_context)

def addCare(request,petID):
    
    if(request.method == 'POST'):
        
        v_form = CareForm(request.POST)
        
        if v_form.is_valid():
            
            user=request.user
            veterinarian=Veterinarian.objects.get(user_id=user.id)
            
            data = v_form.cleaned_data
            
            care = CareAttention(
                motive=data["motive"],
                diagnosis=data["diagnosis"],
                treatment=data["treatment"],
                pet_id=petID,
                vet_id=veterinarian.vet_id,
                veterinarian_id=veterinarian.id
            )
            
            care.save()
            
        return redirect('Gestionar Atenciones')
            
    else:
            
        v_form = CareForm()
            
        return render(request, 'MyCare/addCare.html',{"form": v_form, "petID": petID})
    

def contactDaddy(request, petID):
    
    if(request.method == 'POST'):
        
        v_form = MessageForm(request.POST)
        
        if v_form.is_valid():
            
            user=request.user
            
            pet=Pet.objects.get(id=petID)
            daddy=Daddy.objects.get(id=pet.daddy_id)
            
            data = v_form.cleaned_data
            
            message = Message(
                sender_user_id=user.id,
                receiver_user_id=daddy.user_id,
                message=data['message']
            )
            
            message.save()
            
        return redirect('Gestionar Atenciones')
            
    else:
            
        v_form = MessageForm()
            
        return render(request, 'MyCare/contactDaddy.html',{"form": v_form, "petID": petID})
    
    
def messages(request):
    
    user=request.user
    
    messages = Message.objects.filter(receiver_user_id=user.id)
    v_context = {"messages":messages}          
            
    return render(request, 'MyCare/messages.html',v_context)

def replayDaddy(request, daddyID):
    
    if(request.method == 'POST'):
        
        v_form = MessageForm(request.POST)
        
        if v_form.is_valid():
            
            user=request.user
            
            data = v_form.cleaned_data
            
            message = Message(
                sender_user_id=user.id,
                receiver_user_id=daddyID,
                message=data['message']
            )
            
            message.save()
            
        return redirect('Mensajes de Veterinario')
            
    else:
            
        v_form = MessageForm()
            
        return render(request, 'MyCare/replyDaddy.html',{"form": v_form, "daddyID": daddyID})