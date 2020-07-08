from django.contrib import admin
from django.urls import path,include
from travelapp import views

urlpatterns = [

    path('', views.home,name='home'),
    path('about', views.about,name='about'),
    path('bus', views.bus,name='bus'),
    path('plane', views.plane,name='plane'),
    path('train', views.train,name='train'),
    path('others', views.others,name='others'),
    path('contact', views.contact,name='contact'),
    path('mumbai', views.mumbai,name='mumbai'),
    path('signup', views.signup,name='signup'),
    path('signin', views.signin,name='signin'),

]