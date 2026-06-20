from django.shortcuts import render,redirect

from .forms import *
from .models import *

# Create your views here.


def home(request):
    total=Student.objects.count()
    morning=Student.objects.filter(batch='morning').count()
    evening=Student.objects.filter(batch='evening').count()
    afternoon=Student.objects.filter(batch='afternoon').count()
    software=Student.objects.filter(domain='software').count()
    accounts=Student.objects.filter(domain='accounts').count()
    multimedia=Student.objects.filter(domain='multimedia').count()
    hardware=Student.objects.filter(domain='hardware').count()
    kevin=Student.objects.filter(staff='kevin').count()
    kannan=Student.objects.filter(staff='kannan').count()
    sairam=Student.objects.filter(staff='sairam').count()
    bala=Student.objects.filter(staff='bala').count()

    context={'total':total,'morning':morning,'evening':evening,'afternoon':afternoon,'software':software,
             'accounts':accounts,'multimedia':multimedia,'hardware':hardware,'kevin':kevin,
             'kannan':kannan,'sairam':sairam,'bala':bala}

    return render(request,'home.html',context)


def show(request):
    will=Student.objects.all()
    return render(request,'show.html',{'products':will})

def add(request):
    form=StudentForm()
    if request.method=='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')     
    return render(request,'add.html', {'products': form})

def update(request,id):
    student=Student.objects.get(id=id)
    form=StudentForm(instance=student)
    if request.method=='POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('show')
    return render(request,'add.html', {'products': form})        

def delete(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('show')

def total(request):
    return redirect('show')

def morning(request):
    will=Student.objects.filter(batch="morning")
    return render(request,"show.html",{"products":will})

def afternoon(request):
    will=Student.objects.filter(batch="afternoon")
    return render(request,"show.html",{"products":will})

def evening(request):
    will=Student.objects.filter(batch="evening")
    return render(request,"show.html",{"products":will})

def software(request):
    will=Student.objects.filter(domain="software")
    return render(request,"show.html",{"products":will})
def accounts(request):
    will=Student.objects.filter(domain="accounts")
    return render(request,"show.html",{"products":will})
def multimedia(request):
    will=Student.objects.filter(domain="multimedia")
    return render(request,"show.html",{"products":will})
def hardware(request):
    will=Student.objects.filter(domain="hardware")
    return render(request,"show.html",{"products":will})


def kevin(request):
    will=Student.objects.filter(staff="kevin")
    return render(request,"show.html",{"products":will})
def kannan(request):
    will=Student.objects.filter(staff="kannan")
    return render(request,"show.html",{"products":will})
def sairam(request):
    will=Student.objects.filter(staff="sairam")
    return render(request,"show.html",{"products":will})
def bala(request):
    will=Student.objects.filter(staff="bala")
    return render(request,"show.html",{"products":will})




