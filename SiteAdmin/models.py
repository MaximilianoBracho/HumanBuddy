from sqlite3 import Timestamp
from django.db import models

class Entity(models.Model):
    creation_date=models.DateField(auto_now_add=True)
    active=models.BooleanField()

class Company(Entity):
    
    fiscal_id=models.CharField('CUIT',max_length=11)   
    fiscal_name=models.CharField('Razon Social',max_length=100)
    name=models.CharField('Nombre de Veterinaria',max_length=100)
    start_date=models.DateField('1990-01-01', auto_now=False, auto_now_add=False)
    fiscal_address=models.CharField('Direccion Fiscal',max_length=100)
    real_address=models.CharField('Direccion Real',max_length=100)
    phone=models.CharField('Teléfono',max_length=20)
    mail=models.EmailField()

    
class Person(Entity):
    
    person_id=models.CharField('DNI',max_length=8) 
    name=models.CharField('Nombre',max_length=50)
    surname=models.CharField('Apellido',max_length=50)
    birthdate=models.DateField('01/01/1990', auto_now=False, auto_now_add=False)
    address=models.CharField('Domicilio',max_length=100)
    phone=models.CharField('Teléfono',max_length=20)
    cellphone=models.CharField('Celular',max_length=20)
    mail=models.EmailField()
    
    
class Employee(Person):
    
    fiscal_id=models.CharField('CUIL',max_length=11)
    cargo=models.CharField('Cargo',max_length=50)
    company_id=models.IntegerField()
    
    
class Animal(Entity):
    
    species=models.CharField('Especie',max_length=50)
    family=models.CharField('Familia',max_length=50)
    race=models.CharField('Raza',max_length=50)
    color=models.CharField('Color',max_length=50)
    description=models.CharField('Descripción',max_length=200)
    
class Transaction(models.Model):
    
    timestamp=models.DateTimeField(auto_now_add=True)
    type=models.CharField('Tipo de Transacción',max_length=20)
    