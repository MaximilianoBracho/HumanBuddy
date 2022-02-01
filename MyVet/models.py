from django.db import models
from SiteAdmin.models import Company, Employee

class Vet(Company):
    pass
    
class Veterinarian(Employee):
    
    license=models.CharField('Licencia',max_length=11,default="")
    
class Employee(Employee):
    
    pass
