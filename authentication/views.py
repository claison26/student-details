from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from .models import *
# Create your views here.

def loginpage(request):
    context={"error":''}
    if request.method == 'POST':
        user=authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home') 
        else: 
            context={"error": "Invalid username or password"}
            return render(request, 'login.html', context)
    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('loginpage') 

def signuppage(request):
    context={"error":""}
    if request.method == 'POST':
        
        user_check=User.objects.filter(username=request.POST['username'])
        if user_check.exists():
            context={"error": "Username already exists"}
            return render(request, 'signup.html', context)
        else:
            new_user=User(username=request.POST['username'], first_name=request.POST['first_name'],
                   last_name=request.POST['last_name'], age=request.POST['age'],email=request.POST['email'])
            new_user.set_password(request.POST['password'])
            new_user.save()
            return redirect('loginpage')

    return render(request,'signup.html', context)

