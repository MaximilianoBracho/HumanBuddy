from django.db import models
from SiteAdmin.models import Person, Animal

class Daddy(Person):
    user_id=models.IntegerField('Usuario',null=True)
    
class Pet(Animal):
    
    nickname=models.CharField('Nombre',max_length=50,default="")
    birthdate=models.DateField('Fecha de Nacimiento',auto_now_add=False,auto_now=False,null=True)
    daddy_id=models.IntegerField('Usuario Padre')
    vet_id=models.IntegerField('Veterinaria',null=True)
