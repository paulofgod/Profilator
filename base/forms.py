from django import forms
from django.forms import ModelForm
from .models import Login, Bio


# create a venue form

class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = ('name', 'email')


        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your name'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter a valid email address'})

        }


class BioForm(ModelForm):
    class Meta:
        model = Bio
        fields = ('name','image','description','author1','author2','author1_link_facebook','author2_link_linkedin')


        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your name'}),
            'image': forms.FileInput(attrs={'class':'form-control', 'placeholder':'Select a Photo'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Describe your role'}),
            'author1': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter link'}) ,
            'author2': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter 2nd link'}),
            'author1_link_facebook': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter link'}),
            'author2_link_linkedin': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter 2nd link'})

        }