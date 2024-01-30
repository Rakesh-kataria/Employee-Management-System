from django.shortcuts import render,HttpResponse
from .models import Employee, Role, Department
from datetime import datetime 
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context ={
        'emps':emps
    }
    return render(request,'all_emp.html',context)
    
def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept= int(request.POST['dept'])
        Salary =int(request.POST['Salary'])
        Bonus =int(request.POST['Bonus'])
        Role = int(request.POST['Role'])
        Phone = int(request.POST['Phone'])
        # Hire_date = request.POST('Hire_date')
        new_emp = Employee(first_name= first_name, last_name=last_name, dept_id=dept,Salary=Salary,Bonus=Bonus,Role_id = Role,Phone=Phone,Hire_date =datetime.now())
        new_emp.save()
        return HttpResponse('Employee added Successfully')
    elif request.method =='GET':   
        return render(request,'add_emp.html')
    else:
        return HttpResponse('404 Erroe Not Found !')

def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Succesfully !")
        except:
            return HttpResponse("Please Enter A Valid Employee ID !")
    emps = Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        Role = request.POST['Role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains =name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(Q(dept__name__icontains = dept))
        if Role:
            emps = emps.filter(Q(Role__name__icontains = Role))
        context ={
            'emps':emps
        }
        return render(request,'all_emp.html',context)
    elif request.method == 'GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse("Error 404 Not Found !")