from django.db import models
from datetime import datetime , date

# Create your models here.

class Destination(models.Model):

    place = models.CharField(max_length=122)
    desc = models.TextField()
    price = models.FloatField()
    image = models.ImageField()
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.place

class Crouselimages(models.Model):

    crouselimg1 = models.ImageField()
    crouselimg2 = models.ImageField()
    crouselimg3 = models.ImageField()

   # crouselimg=[crouselimg1,crouselimg2,crouselimg3]


    crouselabel1 = models.CharField(max_length=222)
    crouselabel2 = models.CharField(max_length=222)
    crouselabel3 = models.CharField(max_length=222)

    #crousellabel=[crouselabel1,crouselabel2,crouselabel3]

    crouseltext1 = models.CharField(max_length=222)
    crouseltext2 = models.CharField(max_length=222)
    crouseltext3 = models.CharField(max_length=222)

    
    #crouseltext = [crouseltext1,crouseltext2,crouseltext3]

class Review(models.Model):

    name = models.CharField(max_length=255)
    textreview = models.TextField()
    userdate = models.DateTimeField(default = datetime.now())

    def __str__(self):
        return self.name  


class Bus(models.Model):

    Starting = models.CharField(max_length=255)
    Ending = models.CharField(max_length=255)
    Date = models.DateField()

#to save data with name in database

    def __str__(self):
        return self.Starting  +'-to-'+  self.Ending