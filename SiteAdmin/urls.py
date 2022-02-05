from django.urls import path
from SiteAdmin import views

urlpatterns = [
    path('',views.manage, name="Gestión de Plataforma"),
    path('vets/',views.manageVets, name="Gestión de Veterinarias"),
    path('vets/add/',views.addVets, name="Alta de Veterinarias"),
    path('vets/edit/<vetID>/',views.editVets, name="Editar Veterinarias"),
    path('vets/delete/<vetID>/',views.deleteVets, name="Eliminar Veterinarias"),
    path('daddies/',views.manageDaddies, name="Gestión de Padres"),
    path('daddies/add/',views.addDaddies, name="Alta de Padres"),
    path('daddies/edit/<daddyID>/',views.editDaddies, name="Editar Padres"),
    path('daddies/delete/<daddyID>/',views.deleteDaddies, name="Eliminar Padres"),
]   