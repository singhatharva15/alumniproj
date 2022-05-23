from turtle import home
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

from dashboard.settings import BASE_DIR
from .models import *
from .forms import CareerForm, ProfileForm


# Create your views here.
def index(request):
    user= CustomUser.objects.all()
    return render(request,"index.html",{'newusers': user})

def updateprofile(request, username):  
    student = CustomUser.objects.get(username = username)
    form = ProfileForm(request.POST or None, instance= student)  
    if form.is_valid():  
        form.save()  
        return redirect("/home")
    # else:
    #     return redirect("/index.html") 
    
    return render(request, 'editprofile.html', {'students': student, 'form' : form})

def destroyBatch(request, username, id):  
    car = Career.objects.get(id=id)  
    car.delete()  
    return redirect('/career/'+username) 

def career(request, username):  
    if request.method == "POST":  
        form = CareerForm(request.POST, initial={'account': username})  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/career/'+username)  
            except:  
                pass  
    else:  
        form = CareerForm(initial={'account': username}) 
    exp = Career.objects.raw('SELECT * FROM alumni_Career WHERE account = %s', [username]) 
    return render(request,'career.html',{'form':form, 'exp': exp})


def events(request):
    even= Events.objects.all()
    return render(request,"events.html",{'events': even})

def opportunity(request):
    opp= Opportunities.objects.all()
    return render(request,"opportunity.html",{'opps': opp})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user= auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/home')

        else:
            messages.info(request,'Your Data is not registered. Contact Admin!')
            return redirect('/')

    else:
        return render(request,'registration/login.html')



def logout(request):
    auth.logout(request)
    return redirect('/')