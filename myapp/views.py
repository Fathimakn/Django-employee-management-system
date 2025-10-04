from django.shortcuts import render, redirect, get_object_or_404
from . models import  Employee
from .forms import Employeeform
# Create your views here.
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here
# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        user_name=request.POST.get('username')
        password_1=request.POST.get('password1')
        password_2=request.POST.get('password2')
        email = request.POST.get('email')
        if password_1==password_2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,'username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=user_name, first_name=first_name ,last_name=last_name ,password=password_1, email=email)
                user.save()
                print('user created')
                return redirect('login')

        else:
                messages.info(request,'passwords doesnt match')
                return redirect('register')

    else:
        return render(request,'register.html')
def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
def logout(request):
        auth.logout(request)
        return redirect('add')
        #return render(request,'logout.html')

#def pagemal(request):
    # request.user.is_authenticated:
       # return render(request, 'pagemal.html')
  #  else:
      #  return redirect('login')

def home(request):
   # if  not request.user.is_authenticated:
       # return redirect('login')
    employee=Employee.objects.values()
    return render(request,'all_employees.html',{'employee': employee})

@login_required
def add(request):
    if request.method=="POST":
        form=Employeeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=Employeeform()

    return render(request,'add.html',{'form':form})
@login_required
def delete(request,id):
    employee=get_object_or_404(Employee,id=id)
    print(employee)
    employee.delete()
    return redirect('home')
@login_required
def update(request,id):
    employee = get_object_or_404(Employee, id=id)
    if request.method=="POST":
        form=Employeeform(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=Employeeform(instance=employee)

    return render(request,'update.html',{'form':form , 'employee':employee})