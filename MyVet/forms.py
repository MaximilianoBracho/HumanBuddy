from dataclasses import fields
from django import forms
from django.forms import ModelForm
from MyVet.models import Vet, Veterinarian, Employee

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
        
class VeterinarianForm(ModelForm):
    
    class Meta:
        model = Veterinarian
        
        fields = ['fiscal_id','person_id','name','surname','birthdate','address','phone','cellphone','mail','user_id','license']
    
        widgets = {
            'birthdate': forms.DateInput(attrs={
                'class':'dateinput',
                'type':'date'
            }),
        }
        
class EmployeeForm(ModelForm):
    
    class Meta:
        model = Employee
        
        fields = ['fiscal_id','person_id','name','surname','birthdate','address','phone','cellphone','mail','user_id']
    
        widgets = {
            'birthdate': forms.DateInput(attrs={
                'class':'dateinput',
                'type':'date'
            }),
        }
        