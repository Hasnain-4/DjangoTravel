from django.db import models

# Create your models here.

class Destination(models.Model):

    place = models.CharField(max_length=122)
    desc = models.TextField()
    price = models.FloatField()
    image = models.ImageField()
    offer = models.BooleanField(default=False)

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