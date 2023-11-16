from django.shortcuts import render,redirect
from django .http import HttpResponse
from . models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required




def signup(request):
    if request.method=="POST": 
        username=request.POST['username'] 
        email=request.POST['email']              
        password=request.POST['password']        
        cnfpassword=request.POST['cnfmpassword']  
        if User.objects.filter(username=username).exists(): 
            messages.info(request,"username already exists") 
            return redirect('signup')                        
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email already taken")
            return redirect('signup')
        elif password != cnfpassword :                     
            messages.info(request,"password mismatch")     
            return redirect('signup')                        
        else:
            user=User.objects.create_user(username=username,email=email,password=password) 
                                                                                         
            user.save();                       
            return redirect('index')             
    else:
        return render(request,'signup.html')     


def Loginn(request):
    if request.method == "POST":          
        username = request.POST['username'] 
        password = request.POST['password']
        user = authenticate(username=username,password=password) # 
        if user is not None :    
            auth.login(request,user) 
            return redirect('index')
        else:
            messages.info(request,"invalid login")
    return render(request,'login.html')


def Logoutt(request):
    auth.logout(request)   
    return redirect ('index')

@login_required
def index(request):
    print(request.user.username)
    questions = Question.objects.all()  
    return render(request, 'index.html', {'questions': questions})