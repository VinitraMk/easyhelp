from django.db import models

# Create your models here.

class Question(models.Model):
    serviceid=models.CharField(max_length=15)
    question=models.CharField(max_length=500)
    typeofservice=models.CharField(max_length=50)
    qstnid=models.CharField(max_length=15)
    asker=models.CharField(max_length=50)
    pubdate=models.DateField()

class Answer(models.Model):
    answer=models.CharField(max_length=1000)
    ansid=models.CharField(max_length=15)
    answerer=models.CharField(max_length=50)
    qstnid=models.CharField(max_length=15)
    pubdate=models.DateField()


