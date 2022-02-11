from django.db import models
from SiteAdmin.models import Company, Employee

class Vet(Company):
    user_id=models.IntegerField(null=True)
    
class Veterinarian(Employee):
    
    license=models.CharField('Licencia',max_length=11,default="")
    user_id=models.IntegerField(null=True)
    vet_id=models.IntegerField(null=True)
    
class Employee(Employee):
    user_id=models.IntegerField(null=True)
    vet_id=models.IntegerField(null=True)

