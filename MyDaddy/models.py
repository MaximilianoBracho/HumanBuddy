from django.db import models
from SiteAdmin import models as SiteAdmin

class Daddy(SiteAdmin.Person):
    pass
    
class Pet(SiteAdmin.Animal):
    
    nickname=models.CharField('Nombre',max_length=50)
    birthdate=models.DateField('01/01/1990', auto_now=False, auto_now_add=False)
    buddy=models.IntegerField()
