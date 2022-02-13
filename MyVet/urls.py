from django.urls import path
from MyVet import views

urlpatterns = [
    path('',views.manage, name="Gestión de Veterinaria"),
    path('add/',views.addVet, name="Alta de Veterinaria"),
    path('edit/<vetID>/',views.editVet, name="Editar Veterinaria"),
    path('delete/<vetID>/',views.deleteVet, name="Eliminar Veterinaria"),
    path('veterinarians/<vetID>/',views.manageVeterinarians, name="Gestión de Veterinarios"),
    path('veterinarians/add/<vetID>/',views.addVeterinarian, name="Alta de Veterinario"),
    path('veterinarians/edit/<vetID>/<veterinarianID>/',views.editVeterinarian, name="Editar Veterinario"),
    path('veterinarians/delete/<vetID>/<veterinarianID>/',views.deleteVeterinarian, name="Eliminar Veterinario"),
    path('employees/<vetID>/',views.manageEmployees, name="Gestión de Empleados"),
    path('employees/add/<vetID>/',views.addEmployee, name="Alta de Empleado"),
    path('employees/edit/<vetID>/<employeeID>/',views.editEmployee, name="Editar Empleado"),
    path('employees/delete/<vetID>/<employeeID>/',views.deleteEmployee, name="Eliminar Empleado")
]