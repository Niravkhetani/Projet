from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee
from django.http import JsonResponse

def disp(request):
    EF          = EmployeeForm()
    Emp         = Employee.objects.all()
    return render(request,'Emp.html',{'EF':EF,'Emp':Emp})

def add(request):
    if request.method=='POST':
        EF          = EmployeeForm(request.POST)
        if EF.is_valid:
            Ename       = request.POST.get('Ename')
            Esalary     = request.POST.get('Esalary')
            Eno         = request.POST.get('Eno')
            if Eno != "":
                print(Eno)
                Edata   = Employee.objects.get(Eno=Eno)
                Edata.Ename     = Ename
                Edata.Esalary   = Esalary
                Edata.save()
            print(Ename,Esalary)
            Edata       = Employee(Ename=Ename,Esalary=Esalary)
            Edata.save()
        p           = list(Employee.objects.values())
        data        = {'p':p}
        return JsonResponse(data)
            

def Edit(request):
    if request.method == "POST":
        print(request.POST.get("Eno"))
        Edata       = Employee.objects.get(Eno=request.POST.get("Eno"))
        data        = {'Eno':Edata.Eno,'Ename':Edata.Ename,'Esalary':Edata.Esalary}
        print(data)
        return JsonResponse(data)

def delete(request):
    if request.method=="POST":
        Emp         = Employee.objects.get(Eno=request.POST.get('Eno'))
        Emp.delete()
        return JsonResponse({'success':'1'})


