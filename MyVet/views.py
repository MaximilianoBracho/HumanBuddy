from ast import And
from django.shortcuts import redirect, render
from MyVet.models import Vet, Veterinarian, Employee
from MyVet.forms import VetForm, VeterinarianForm, EmployeeForm
from django.contrib.auth.models import User, Group

# Create your views here.

def manage(request):
    
    user=request.user
    
    vets = Vet.objects.filter(user_id=user.id)
    v_context = {"vets":vets}          
            
    return render(request, 'MyVet/manage.html',v_context)

def addVet(request):
    
    if(request.method == 'POST'):
        
        v_form = VetForm(request.POST)
        
        if v_form.is_valid():
            
            data = v_form.cleaned_data
            user=request.user
            
            vet = Vet(
                fiscal_id=data["fiscal_id"],
                fiscal_name=data["fiscal_name"],
                name=data["name"],
                start_date=data["start_date"],
                fiscal_address=data["fiscal_address"],
                real_address=data["real_address"],
                phone=data["phone"],
                mail=data["mail"],
                user_id=user.id
            )
            
            vet.save()
            
        return redirect('Gestión de Veterinarias')
            
    else:
            
        v_form = VetForm()
            
        return render(request, 'MyVet/addVet.html',{"form": v_form})
    
def editVet(request,vetID):
    
    vet = Vet.objects.get(id=vetID)
        
    if(request.method == 'POST'):
        
        v_form = VetForm(request.POST, instance=vet)
        
        print(v_form)
        
        if v_form.is_valid():
            
            v_form.save()
            
        return redirect('Gestión de Veterinarias')
            
    else:
            
        v_form = VetForm(initial={
                "fiscal_id":vet.fiscal_id,
                "fiscal_name":vet.fiscal_name,
                "name":vet.name,
                "start_date":vet.start_date,
                "fiscal_address":vet.fiscal_address,
                "real_address":vet.real_address,
                "phone":vet.phone,
                "mail":vet.mail
            })
        
        return render(request, 'MyVet/editVet.html',{"form": v_form, "id":vet.id})
    
def deleteVet(request, vetID):
    
    vet = Vet.objects.get(id=vetID)
    vet.delete()
    
    return redirect('Gestión de Veterinarias')

def manageVeterinarians(request,vetID):
      
    veterinarians = Veterinarian.objects.filter(vet_id=vetID)
    v_context = {"veterinarians":veterinarians,"vetID":vetID}          
            
    return render(request, 'MyVet/manageVeterinarians.html',v_context)

def addVeterinarian(request,vetID):
    
    if(request.method == 'POST'):
        
        v_form = VeterinarianForm(request.POST)
        
        if v_form.is_valid():
            
            data = v_form.cleaned_data

            veterinarian = Veterinarian(
                fiscal_id=data["fiscal_id"],
                person_id=data["person_id"],
                name=data["name"],
                surname=data["surname"],
                birthdate=data["birthdate"],
                address=data["address"],
                phone=data["phone"],
                cellphone=data["cellphone"],
                mail=data["mail"],
                user_id=data["user_id"],
                vet_id=vetID,
                license=data["license"]   
            )
            
            veterinarian.save()
            
            user = User.objects.get(id=veterinarian.user_id)
            group = Group.objects.get(name='Veterinarian')
            user.groups.add(group)
            
        return redirect('Gestión de Veterinarios',veterinarian.vet_id)
            
    else:
            
        v_form = VeterinarianForm()
            
        return render(request, 'MyVet/addVeterinarian.html',{"form": v_form,"vetID":vetID})
    
def editVeterinarian(request,vetID, veterinarianID):
    
    veterinarian = Veterinarian.objects.get(id=veterinarianID, vet_id=vetID)
        
    if(request.method == 'POST'):
        
        v_form = VeterinarianForm(request.POST, instance=veterinarian)
        
        print(v_form)
        
        if v_form.is_valid():
            
            v_form.save()
            
        return redirect('Gestión de Veterinarios',vetID)
            
    else:
            
        v_form = VeterinarianForm(initial={
                "fiscal_id":veterinarian.fiscal_id,
                "person_id":veterinarian.person_id,
                "name":veterinarian.name,
                "surname":veterinarian.surname,
                "birthdate":veterinarian.birthdate,
                "address":veterinarian.address,
                "phone":veterinarian.phone,
                "cellphone":veterinarian.cellphone,
                "mail":veterinarian.mail,
                "user_id":veterinarian.user_id,
                "vet_id":vetID,
                "license":veterinarian.license
            })
        
        return render(request, 'MyVet/editVeterinarian.html',{"form": v_form, "vetID":vetID, "veterinarianID":veterinarian.id}) 
    
def deleteVeterinarian(request, vetID, veterinarianID):
    
    veterinarian = Veterinarian.objects.get(id=veterinarianID, vet_id=vetID)
    veterinarian.delete()
    
    return redirect('Gestión de Veterinarios',vetID)

def manageEmployees(request,vetID):
      
    employees = Employee.objects.filter(vet_id=vetID)
    v_context = {"employees":employees,"vetID":vetID}         
            
    return render(request, 'MyVet/manageEmployees.html',v_context)

def addEmployee(request,vetID):
    
    if(request.method == 'POST'):
        
        v_form = EmployeeForm(request.POST)
        
        if v_form.is_valid():
            
            data = v_form.cleaned_data

            employee = Employee(
                fiscal_id=data["fiscal_id"],
                person_id=data["person_id"],
                name=data["name"],
                surname=data["surname"],
                birthdate=data["birthdate"],
                address=data["address"],
                phone=data["phone"],
                cellphone=data["cellphone"],
                mail=data["mail"],
                user_id=data["user_id"],
                vet_id=vetID
            )
            
            employee.save()
            
            user = User.objects.get(id=employee.user_id)
            group = Group.objects.get(name='Employee')
            user.groups.add(group)
            
        return redirect('Gestión de Empleados',employee.vet_id)
            
    else:
            
        v_form = EmployeeForm()
            
        return render(request, 'MyVet/addEmployee.html',{"form": v_form,"vetID":vetID})
    
def editEmployee(request, vetID, employeeID):
    
    employee = Employee.objects.get(id=employeeID, vet_id=vetID)
        
    if(request.method == 'POST'):
        
        v_form = EmployeeForm(request.POST, instance=employee)
        
        print(v_form)
        
        if v_form.is_valid():
            
            v_form.save()
            
        return redirect('Gestión de Empleados',vetID)
            
    else:
            
        v_form = EmployeeForm(initial={
                "fiscal_id":employee.fiscal_id,
                "person_id":employee.person_id,
                "name":employee.name,
                "surname":employee.surname,
                "birthdate":employee.birthdate,
                "address":employee.address,
                "phone":employee.phone,
                "cellphone":employee.cellphone,
                "mail":employee.mail,
                "user_id":employee.user_id,
                "vet_id":vetID
            })
        
        return render(request, 'MyVet/editEmployee.html',{"form": v_form, "vetID":vetID, "employeeID":employee.id}) 
    
def deleteEmployee(request, vetID, employeeID):
    
    employee = Employee.objects.get(id=employeeID, vet_id=vetID)
    employee.delete()
    
    return redirect('Gestión de Empleados',vetID)