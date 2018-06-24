from django.db import models

# Create your models here.

class Service(models.Model):
    typeofservice=models.CharField(max_length=50)
    startdate=models.DateField()
    nameofservice=models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    seraddr=models.CharField(max_length=200,default=None)
    avgrating=models.FloatField(default=0.0)
    reviewcount=models.IntegerField(default=0)
    serviceid=models.CharField(max_length=15)
    owneremail=models.CharField(max_length=50)
    servicemail=models.CharField(max_length=50,default=None)
    servicephone=models.CharField(max_length=50,default=None)
    websiteurl=models.CharField(max_length=2000,default=None)

class Choice(models.Model):
    iden=models.IntegerField()
    sertype=models.CharField(max_length=50)
