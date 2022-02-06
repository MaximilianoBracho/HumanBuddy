from dataclasses import fields
from django import forms
from django.forms import ModelForm
from MyDaddy.models import Pet

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