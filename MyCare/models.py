from email import message
from django.db import models
from SiteAdmin.models import Transaction

class CareAttention(Transaction):
    
    type="CareAttention"
    motive=models.CharField('Motivo de Consulta',max_length=200,default="")
    diagnosis=models.CharField('Diagnóstico',max_length=200,default="")
    treatment=models.CharField('Tratamiento',max_length=200,default="")
    pet_id=models.IntegerField(null=True)
    vet_id=models.IntegerField(null=True)
    veterinarian_id=models.IntegerField(null=True)
    
class Message(Transaction):
    type="Message"
    sender_user_id=models.IntegerField(null=True)
    receiver_user_id=models.IntegerField(null=True)
    message=models.CharField('Mensaje',max_length=500,default="")
    
