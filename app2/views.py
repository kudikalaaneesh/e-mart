from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import  mobiles
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import logout
from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .forms import Signups,oneplusForm,redmiform
from .models import Signup,oneplus,redmi
# from .models import products
from . import models
from .forms import admin
from .models import mobile

import datetime


def add(request):
    if request.method =='POST':
        username=request.POST['username']
        password_1=request.POST['password_1']
        print(username)
        check=Signup.objects.filter(username__contains=username)
        check1=Signup.objects.filter(password_1__contains=password_1)
        print(check)
        if check and check1:
            form=Signup()
            return render(request,"new.html")
        else:
            return HttpResponse("<h1>wrong password or wrong user name please enter  correct cerdiencts</h1>")
    return render(request, "Login.html")
        


    
       
def signup(request):
    if request.method=="POST":
        form=Signups(request.POST)
        if form.is_valid(): 
            form.save()
            return HttpResponse("<h1> you are sucessfilly registered....</h1>")
        else:
            return HttpResponse("<h1>wrong</h1>")
    else:
        form=Signups()   
        print(form)
        print(form.errors)
    return render(request,'signup.html', {'form':form})



def card(request):
    return render(request,'Card.html', {"numbers":range(10)})

def cart(request):
    return render(request,'cart.html', {"number":range(2)})


def emp(request):
    if request.method == "POST":
        form =EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form =EmployeeForm()
    return render(request,'index.html',{'form':form})





def gg(request):
    return render(request,'new.html')


@login_required
def products(request):
    if request.method=='POST':
        form=admin(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>your data is saved sucessfully.......</h1>")
         
        else:
            return HttpResponse("<h1> UR DATA NOT SAVED PLEASE TRY AGAIN.....</h1>")
    else:
        form=admin()
    return render(request,'products.html',{'form':form})

def productcard(request):

    dd= models.products.objects.all().values()


    return  render(request,'o.html',{'dd':dd})
    

def mproducts(request):
    if request.method=='POST':
        form = mobiles(request.POST)
        if form.is_valid():
            
            form.save()
            return HttpResponse("your data is saves sucessfully")
        else:
            HttpResponse("your data is not saved please try again")
    else:
        form=mobiles()
    return render(request,'mobileproducts.html',{'form':form})


def showmobiles(request):
   mob=models.mobile.objects.all().values()
  
   return render(request,'diaplaymobiles.html',{'mob': mob})

def oneplusmob(request):
    if request.method=="POST":
        form=oneplusForm(request.POST)
        if form.is_valid(): 
            form.save()
            return HttpResponse("<h1> you are sucessfilly registered....</h1>")
        else:
            return HttpResponse("<h1>wrong</h1>")
    else:
        form=oneplusForm()   
        print(form)
        print(form.errors)
    return render(request,'oneplusforms.html', {'form':form})

def one(request):
    one=models.oneplus.objects.all().values()
    return render(request,'showoneplus.html',{'one': one})

def redmim(request):
    if request.method == "POST":
        form = redmiform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1> you are sucessfilly registered....</h1>")
        else:
            return HttpResponse("<h1>wrong</h1>")
    else:
        form = redmiform()
        print(form)
        print(form.errors)
    return render(request, 'redmiforms.html', {'form': form})

def red(request):
    red = models.redmi.objects.all().values()
    return render(request, 'showredmi.html', {'red': red})


def logout_view(request):
    logout(request)
    return redirect('Login/')
    

def bas(request):
    return render(request,"home.html")
