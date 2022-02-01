from django.db import models
from SiteAdmin.models import Transaction

class CareAttention(Transaction):
    
    motive=models.CharField('Motivo de Consulta',max_length=200,default="")
    diagnosis=models.CharField('Diagnóstico',max_length=200,default="")
    treatment=models.CharField('Tratamiento',max_length=200,default="")
    
