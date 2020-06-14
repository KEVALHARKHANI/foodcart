from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from .models import userdata
from django.contrib.auth.models import auth,User
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter,OrderingFilter

# Create your views here.
def login(request):
    return render(request,"login.html")
def submit(request):
    user = request.POST['username']
    password = request.POST['password']
    user =auth.authenticate(username=user,password=password)
    if user is not None:
        request.session['refresh']="false"
        auth.login(request,user)
        return redirect('home')

    else:
        messages.info(request,"invalid username or password")
        return render(request,'login.html',{'error':'worng user name','show':'nhgy'})

def register(request):
    return render(request,'register.html')

def vali(request):
    firstname=request.POST['fn']
    lastname = request.POST['ln']
    print(lastname)
    name= firstname+" "+lastname
    username = request.POST['username']
    bd = request.POST['birthdate']
    phone = request.POST['phone']
    email = request.POST['email']
    password = request.POST['password']
    gender=request.POST['gender']
    if User.objects.filter(username=username).exists():
        messages.info(request,'username exists!')
        return redirect('register')
    else:
        data = User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
        user_data=User.objects.filter(username=username)
        for i in user_data:
            user_id=i.id
        udata= userdata(user_id=user_id,name=name,username=username,birthdate=bd,phone=phone,email=email,password=password,gender=gender)
        print(password)
        data.save()
        udata.save()
        return redirect('/?check=true')