from django.shortcuts import render , redirect

from .models import Destination, Crouselimages
from django.contrib.auth.models import User , auth

# Create your views here.

def home(request):

    dests= Destination.objects.all()
    dests1 = Crouselimages.objects.all()

    return render(request,'base.html', {'dests':dests , 'dests1':dests1})

def about(request):

    return render(request,'about.html')

def bus(request):

    return render(request,'bus.html')

def plane(request):

    return render(request,'plane.html')

def train(request):

    return render(request,'train.html')

def others(request):

    return render(request,'others.html')

def contact(request):

    return render(request,'contact.html')

def mumbai(request):

    return render(request,'mumbai.html')

def signup(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:

            if User.objects.filter(username=username).exists():
                print('User Exists')
            elif User.objects.filter(email=email):
                print('Email Already Taken')

            else:
                user = User.objects.create_user(username=username ,password= password1 , email= email ,first_name=first_name , last_name = last_name)
                user.save()
                

        else: 
           print('password is not matching!!')    
        return redirect("/")


    else:
        
        return render(request,'signup.html')

def signin(request):

    return render(request,'signin.html')
