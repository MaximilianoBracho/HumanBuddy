from sqlite3 import Timestamp
from django.db import models

class Entity(models.Model):
    creation_date=models.DateField(auto_now_add=True)
    active=models.BooleanField(default=True)
    
    class Meta:
        abstract = True

class Company(Entity):
    
    fiscal_id=models.CharField('CUIT',max_length=11,default="")   
    fiscal_name=models.CharField('Razón Social',max_length=100,default="")
    name=models.CharField('Nombre de Veterinaria',max_length=100,default="")
    start_date=models.DateField('Fecha de Inscripción',auto_now_add=False,auto_now=False,null=True)
    fiscal_address=models.CharField('Dirección Fiscal',max_length=100,default="")
    real_address=models.CharField('Dirección Real',max_length=100,default="")
    phone=models.CharField('Teléfono',max_length=20,default="")
    mail=models.EmailField(default="info@mail.com")
    
    class Meta:
        abstract = True

    
class Person(Entity):
    
    person_id=models.CharField('DNI',max_length=8,default="") 
    name=models.CharField('Nombre',max_length=50,default="")
    surname=models.CharField('Apellido',max_length=50,default="")
    birthdate=models.DateField('Fecha de Nacimiento',auto_now_add=False,auto_now=False,null=True)
    address=models.CharField('Domicilio',max_length=100,default="")
    phone=models.CharField('Teléfono',max_length=20,default="")
    cellphone=models.CharField('Celular',max_length=20,default="")
    mail=models.EmailField(default="info@mail.com")
    
    class Meta:
        abstract = True
    
    
class Employee(Person):
    
    fiscal_id=models.CharField('CUIL',max_length=11,default="")
    cargo=models.CharField('Cargo',max_length=50,default="")
    company_id=models.IntegerField()
    
    class Meta:
        abstract = True
    
    
class Animal(Entity):
    
    species=models.CharField('Especie',max_length=50,null=True,default="")
    family=models.CharField('Familia',max_length=50,null=True,default="")
    race=models.CharField('Raza',max_length=50,null=True,default="")
    color=models.CharField('Color',max_length=50,null=True,default="")
    description=models.CharField('Descripción',null=True,max_length=200,default="")
    
    class Meta:
        abstract = True
    
class Transaction(models.Model):
    
    timestamp=models.DateTimeField(auto_now_add=True)
    type=models.CharField('Tipo de Transacción',max_length=20,default="")
    
    class Meta:
        abstract = True
    