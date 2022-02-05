from dataclasses import fields
from typing_extensions import Required
from django import forms
from django.forms import ModelForm, fields_for_model
from numpy import require
from MyVet.models import Vet, Veterinarian, Employee
from MyDaddy.models import Daddy, Pet

class VetForm(ModelForm):
    
    class Meta:
        model = Vet
        
        fields = ['fiscal_id','fiscal_name','name','start_date','fiscal_address','real_address','phone','mail']
        
        widgets = {
            'start_date': forms.DateInput(attrs={
                'class':'dateinput',
                'type':'date'
            }),
        }
        
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


