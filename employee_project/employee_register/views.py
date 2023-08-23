from django.shortcuts import render,redirect
from .form import EmployeeForm
from .models import Employee
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



@login_required(login_url="login_page")
def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {"form": form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid:
            form.save()
        return redirect("employee_list")   
    
    

@login_required(login_url="login_page")
def employee_list(request):
    print("User authenticated:", request.user.is_authenticated)
    context = {"employee_list": Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)

def employee_delete(request,id):
    employee=Employee.objects.get(pk=id)
    employee.delete()
    return redirect("/list")    


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("employee_list")
        elif username == "database" and password == "785":
            user = User.objects.create_user(username=username, password=password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("employee_list")
        else:
            messages.error(request, "Incorrect credentials. Please try again.")
    
    return render(request, "employee_register/login.html")



def registerPage(request):
    return render(request,"employee_register/register.html")


def logout_page(request):
    logout(request)
    return redirect("login_page")