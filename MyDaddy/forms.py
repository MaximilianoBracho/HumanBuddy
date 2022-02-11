from dataclasses import fields
from django import forms
from django.forms import ModelForm
from MyDaddy.models import Daddy, Pet

class DaddyForm(ModelForm):
    
    class Meta:
        model = Daddy
    
        fields = ['person_id','name','surname','birthdate','address','phone','cellphone','mail']
    
        widgets = {
            'birthdate': forms.DateInput(attrs={
                'class':'dateinput',
                'type':'date'
            }),
        }
        
class PetForm(ModelForm):
    
    class Meta:
        model = Pet
        
        fields = ['species','family','race','color','nickname','birthdate','vet_id']
        
        widgets = {
            'birthdate': forms.DateInput(attrs={
                'class':'dateinput',
                'type':'date'
            }),
        }