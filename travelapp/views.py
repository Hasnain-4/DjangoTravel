from django.shortcuts import render

from .models import Destination, Crouselimages

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
