from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse
from .models import Question
import time,datetime
# Create your views here.

class Forum(View):
    template_name='forum/forum.html'

    def get(self,request):
        qstnobj=Question.objects.all()
        return render(request,self.template_name,{'qstns':qstnobj})

class AskQuery(View):
    template_name='forum/ask.html'
    
    def get(self,request):
        return render(request,self.template_name,{})


def query(request):
    usermail=request.session.get('uemail',None)
    if request.method=='POST' and usermail!=None:
        serid=request.session.get('serid',None)
        sertype=request.session.get('sertype',None)
        if serid==None or sertype==None:
            return render(request,'home/error.html',{'main_error':'Internal Server Error. Try again after a few minutes'})
        data=request.POST['query']
        st=datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
        dt=datetime.date.today().strftime('%Y-%m-%d')
        #return HttpResponse(data)
        qstnobj=Question(serviceid=serid,question=data,typeofservice=sertype,asker=usermail,qstnid=st,pubdate=dt)
        qstnobj.save()
        #return HttpResponse(qstnobj)
        return redirect('/forum')
    else:
        return render(request,'home/error.html',{'main_error':'User has logged out'})
