from django.urls import path, re_path
from MyCare import views 

urlpatterns = [
    path('',views.manage,name="Gestionar Atenciones"),
    path('care/add/<petID>/',views.addCare, name="Atender Mascota"),
    path('contact/add/<petID>/',views.contactDaddy, name="Contactar Padre"),
    path('messages',views.messages, name="Mensajes de Veterinario"),
    path('message/replay/<daddyID>/',views.replayDaddy, name="Responder Padre")
]