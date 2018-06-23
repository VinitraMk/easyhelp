from django import forms
from .models import User
from django.forms import ModelForm

class UserForm(ModelForm):
    name = forms.CharField(
            label = 'Name',
            required = True,
            max_length = 100,
            widget = forms.TextInput(
                attrs = {'class': 'form-control', 'name': 'name', 'autofocus':True})
            )
    email= forms.CharField(
            label = 'Email',
            required = True,
            max_length = 50,
            widget = forms.TextInput(
                attrs = {'class': 'form-control', 'name': 'email','type':'email'})
            )
    password= forms.CharField(
            label = 'Password',
            required = True,
            max_length = 50,
            widget = forms.TextInput(
                attrs = {'class': 'form-control', 'name': 'password','type':'password'})
            )
    '''phoneno= forms.CharField(
            label = 'Contact No',
            max_length = 15,
            required = True,
            widget = forms.TextInput(
                attrs = {'class':'form-control','name':'phoneno','type':'password'})
            )'''

    class Meta:
        model=User
        fields=['name','email','password']


class LoginForm(ModelForm):

    email= forms.CharField(
            label = 'Email',
            max_length = 100,
            required = True,
            widget = forms.TextInput(
                attrs = {'class': 'form-control', 'name': 'email','type':'email'})
            )
    password= forms.CharField(
            label = 'Password',
            max_length = 100,
            required = True,
            widget = forms.TextInput(
                attrs = {'class': 'form-control', 'name': 'password','type':'password'})
            )

    
    class Meta:
        model=User
        fields=['email','password']


