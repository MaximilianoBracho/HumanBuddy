from django.db import models
from SiteAdmin import models as SiteAdmin

class Vet(SiteAdmin.Company):
    pass
    
class Veterinarian(SiteAdmin.Employee):
    
    license=models.CharField('Licencia',max_length=11)
    
class Employee(SiteAdmin.Employee):
    
    pass
