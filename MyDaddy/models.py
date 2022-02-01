from django.db import models
from SiteAdmin.models import Person, Animal

class Daddy(Person):
    pass
    
class Pet(Animal):
    
    nickname=models.CharField('Nombre',max_length=50,default="")
    birthdate=models.DateField('1950-01-01',default="1950-01-01")
    buddy_id=models.IntegerField()
