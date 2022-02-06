from dataclasses import fields
from django import forms
from django.forms import ModelForm
from MyVet.models import Vet
from MyDaddy.models import Daddy

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


