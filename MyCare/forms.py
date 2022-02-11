from django.forms import ModelForm
from MyCare.models import CareAttention, Message

class CareForm(ModelForm):
    
    class Meta:
        model = CareAttention
    
        fields = ['motive','diagnosis','treatment']
        
class MessageForm(ModelForm):
    
    class Meta:
        model = Message
    
        fields = ['message']