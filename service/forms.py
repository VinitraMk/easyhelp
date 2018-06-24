from django.forms import ModelForm
from .models import Service
from django import forms
class ServiceForm(ModelForm):
    SERVICE_CHOICES = [
            (1,'Accounting'),
            (2,'Consulting'),
            (3,'Legal'),
            (4,'Tax'),
            (5,'Marketing'),
            (6,'Web Design'),
            (7,'Writing & Translation'),
            (8,'Design & Multimedia'),
            (9,'Home Decor'),
            (10,'Event Planner'),
            (11,'Other'),
            ]

    typeofservice=forms.ChoiceField(
            choices=SERVICE_CHOICES,
            widget=forms.Select(attrs={'class':'form-control','autofocus':True})
            )
            

    nameofservice=forms.CharField(
            label='Name of Service/Company',
            max_length=50,
            widget=forms.TextInput(attrs={'class':'form-control'})
            )

    startdate=forms.DateField(
            widget=forms.TextInput(
                attrs={'class':'form-control','id':'datepicker'})
            )

    description=forms.CharField(
            max_length=6000,
            widget=forms.Textarea(attrs={'class':'form-control','rows':'7'})
            )


    servicephone=forms.CharField(
            required=False,
            max_length=15,
            widget=forms.TextInput(attrs={'class':'form-control','type':'tel'})
            )

    websiteurl=forms.CharField(
            required=False,
            max_length=2000,
            widget=forms.TextInput(attrs={'class':'form-control','type':'url'})
            )

    servicemail=forms.CharField(
            required=False,
            max_length=50,
            widget=forms.TextInput(attrs={'class':'form-control','type':'email'})
            )

    owneremail=forms.CharField(
            required=False,
            widget=forms.HiddenInput()
            )

    serviceid=forms.CharField(
            required=False,
            widget=forms.HiddenInput()
            )

    seraddr=forms.CharField(
            required=False,
            label='Business Location Address',
            max_length=248,
            widget=forms.TextInput(attrs={'class':'form-control'})
            )

    class Meta:
        model=Service
        fields=['typeofservice','nameofservice','startdate','description','servicephone','websiteurl','servicemail','seraddr','owneremail',
                'serviceid']


class UpdateServiceForm(ModelForm):

    SERVICE_CHOICES = [
            (1,'Accounting'),
            (2,'Consulting'),
            (3,'Legal'),
            (4,'Tax'),
            (5,'Marketing'),
            (6,'Web Design'),
            (7,'Writing & Translation'),
            (8,'Design & Multimedia'),
            (9,'Home Decor'),
            (10,'Event Planner'),
            (11,'Other'),
            ]

    typeofservice=forms.ChoiceField(
            choices=SERVICE_CHOICES,
            widget=forms.Select(attrs={'class':'form-control','autofocus':True})
            )
            

    nameofservice=forms.CharField(
            label='Name of Service/Company',
            max_length=50,
            widget=forms.TextInput(attrs={'class':'form-control'})
            )

    startdate=forms.DateField(
            widget=forms.TextInput(
                attrs={'class':'form-control','id':'datepicker'})
            )

    description=forms.CharField(
            max_length=6000,
            widget=forms.Textarea(attrs={'class':'form-control','rows':'7'})
            )


    servicephone=forms.CharField(
            required=False,
            max_length=15,
            widget=forms.TextInput(attrs={'class':'form-control','type':'tel'})
            )

    websiteurl=forms.CharField(
            required=False,
            max_length=2000,
            widget=forms.TextInput(attrs={'class':'form-control','type':'url'})
            )

    servicemail=forms.CharField(
            required=False,
            max_length=50,
            widget=forms.TextInput(attrs={'class':'form-control','type':'email'})
            )

    seraddr=forms.CharField(
            required=False,
            label='Business Location Address',
            max_length=248,
            widget=forms.TextInput(attrs={'class':'form-control'})
            )

    class Meta:
        model=Service
        fields=['typeofservice','nameofservice','startdate','description','servicephone','websiteurl','servicemail','seraddr']


