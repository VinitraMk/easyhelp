from django.db import models

# Create your models here.

class Service(models.Model):
    typeofservice=models.CharField(max_length=50)
    startdate=models.DateField()
    nameofservice=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    seraddr=models.CharField(max_length=200)
    avgrating=models.FloatField()
    serviceid=models.CharField(max_length=15)
    owneremail=models.CharField(max_length=50)

