from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse
from service.models import Choice as ChoiceModel
from login.models import User as UserModel
from .models import Answer as AnsModel
from .models import Question
import time,datetime
# Create your views here.

class Forum(View):
    template_name='forum/forum.html'

    def get(self,request):
        qstnobj=Question.objects.all()
        return render(request,self.template_name,{'qstns':qstnobj})

class Filter(View):
    template_name='forum/forum.html'

    def get(self,request):
        data=int(request.get_full_path().split('/')[-1])
        ch=ChoiceModel.objects.get(iden=data).sertype
        serobj=Question.objects.filter(typeofservice=ch).all()
        return render(request,self.template_name,{'qstns':serobj,'filter':ch})
        #return HttpResponse('hello')

class Answer(View):
    template_name='forum/answer.html'

    def get(self,request):
        data=request.get_full_path()
        data=data[-14:]
        ansobj=AnsModel.objects.filter(qstnid=data).all()
        prbst=Question.objects.get(qstnid=data).question
        request.session.set_expiry(3600)
        request.session['qstnid']=data
        return render(request,self.template_name,{'anss':ansobj,'stmnt':prbst,'qstnid':data})
        #return HttpResponse(data)
    

class AskQuery(View):

    def post(self,request):
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


class AnsQuery(View):

    def post(self,request):
        usermail=request.session.get('uemail',None)
        if request.method=='POST' and usermail!=None:
            qstnid=request.session.get('qstnid',None)
            if qstnid==None:
                return render(request,'home/error.html',{'main_error':'Internal Server Error. Try again after a few minutes'})
            data=request.POST['answer']
            dt=datetime.date.today().strftime('%Y-%m-%d')
            st=datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
            ansobj=AnsModel(qstnid=qstnid,answerer=usermail,answer=data,pubdate=dt,ansid=st)
            ansobj.save()
            ansobj=AnsModel.objects.filter(qstnid=qstnid).all()
            prbst=''
            try:
                prbst=Question.objects.get(qstnid=qstnid).question
            except:
                prbst=''
            url='/getanswers/id='+qstnid
            request.session['qstnid']=qstnid
            return redirect(url)
        else:
            return render(request,'home/error.html',{'main_error':'User has logged out'})

        
