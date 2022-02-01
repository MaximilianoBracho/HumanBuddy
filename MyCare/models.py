from django.db import models
from SiteAdmin import models as SiteAdmin

class CareAttention(SiteAdmin.Transaction):
    
    motive=models.CharField('Motivo de Consulta',max_length=200)
    diagnosis=models.CharField('Diagnóstico',max_length=200)
    treatment=models.CharField('Tratamiento',max_length=200)
    
