from django.contrib import admin

from .models import Destination,Crouselimages,Review , Bus, Contact

# Register your models here.

admin.site.register(Destination)
admin.site.register(Crouselimages)

admin.site.register(Review)
admin.site.register(Bus)
admin.site.register(Contact)