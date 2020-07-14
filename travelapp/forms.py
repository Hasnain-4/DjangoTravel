from django import forms

from .models import Review 

class UserReview(forms.ModelForm):

    class Meta:
        model = Review
        fields =[

        'name',
        'textreview',
        'userdate'
        ]

class DateForm(forms.Form):
    date = forms.DateField()
    

