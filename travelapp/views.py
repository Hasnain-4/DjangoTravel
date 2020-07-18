from django.shortcuts import render , redirect

from .models import Destination, Crouselimages , Review
    
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .models import Bus

import random

from .forms import UserReview

# Create your views here.

def home(request):

    dests= Destination.objects.all()
    dests1 = Crouselimages.objects.all()
    obj = Review.objects.all()

    return render(request,'base.html', {'dests':dests , 'dests1':dests1,'obj': obj})

def about(request):

    return render(request,'about.html')

def bus(request):

    if request.method == 'POST':

        starting = request.POST.get('starting')
        ending = request.POST.get('ending')
        date = request.POST.get('date')

        n = random.randint(322,622)

        bususer = Bus(Starting = starting , Ending = ending , Date = date)
        bususer.save()

        bus = Bus.objects.all()

        return render(request,'ticket.html' , {'starting' : starting,'ending' : ending,'date' : date, 'n' : n, 'bus' : bus} )


        messages.success(request, "The record has been saved successfully!")
        

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
                messages.warning(request, 'This username is already taken')
                return redirect("signup")
            elif User.objects.filter(email=email):
                messages.warning(request, 'This email is already taken , Please try other one!')
                return redirect("signup")

            else:
                user = User.objects.create_user(username=username ,password= password1 , email= email ,first_name=first_name , last_name = last_name)
                user.save()
                messages.success(request, 'Successfully Register! Now Please Login With Your Credentials') 
                return redirect("signin")
                    

        else:
            messages.warning(request, 'Password is not matching')  
            return redirect("signup")
                
    else:
        
        return render(request,'signup.html')

def signin(request):

    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username , password = password )

        if user is not None:
            auth.login(request , user)
            return redirect ("/")

        else:
            
            messages.warning(request, 'Please Enter Valid Username & Password')  
            return redirect ("signin")
    else:
        return render(request,'signin.html')
        
def logout(request):

    auth.logout(request)
    return redirect("/")

    #Adding a comment for commitment


#not able to mapped the url that's why this function is here...
def review(request):

    form = UserReview(request.POST or None)
    if form.is_valid():
        form.save()
        form = UserReview()
    
    context = {
        'form' : form,
        
    }

    return render(request,'review.html' , context)


def search(request):

    
    query = request.GET['query']

    if len(query)>88:
        alldest = Destination.objects.none()
    else:    
        destplace = Destination.objects.filter(place__icontains=query)
        destdesc = Destination.objects.filter(desc__icontains=query)
        alldest = destplace.union(destdesc)

    if alldest.count() == 0:
        messages.warning(request, "No search result found, please refine your query")
        
    params = {'alldest' : alldest , 'query' : query}
    return render(request,'search.html' , params)

def ticket(request):

    starting = request.GET.get('starting')
    ending = request.GET.get('ending')
    date = request.GET.get('date')

    print(starting)

    #data = Bus.objects.all()
    n = random.randint(122,2222)

    return render(request,'ticket.html' , {'n' : n })
