from django.shortcuts import render,redirect
from .models import Service as ServiceModel
from .models import Choice as ChoiceModel
from .models import ReviewRate
from .forms import ServiceForm,UpdateServiceForm
from django.views.generic import View
import time,datetime
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.

class Service(View):
    template_name='service/formpage.html'

    def get(self,request):
        form_user=ServiceForm()
        return render(request,self.template_name,{'form_user':form_user})

    def post(self,request):
        form_user=ServiceForm(request.POST)
        if form_user.is_valid():
            if request.session.get('uemail',None)!=None:
                st=datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
                #print('st',st)
                user=form_user.save(commit=False)
                user.serviceid=st
                user.owneremail=request.session['uemail']
                #print('st',user.owneremail,user.serviceid)
                user.save()
                return redirect('/profile')
            else:
                return render(request,'home/error.html',{'main_error':'Logged out of session'})
        else:
            #request.session['error']='form invalid'
            return render(request,'home/error.html',{'main_error':'Errors in form input','form':form_user})


class YourServices(View):
    template_name='service/servicelist.html'

    def get(self,request):
        uemail=request.session['uemail']
        serobj=ServiceModel.objects.filter(owneremail=uemail).all()
        return render(request,self.template_name,{'serobj':serobj})

class AllServices(View):
    template_name='service/allservices.html'

    def get(self,request):
        serobj=ServiceModel.objects.all()
        return render(request,self.template_name,{'serobj':serobj})

class ServiceInfo(View):
    template_name='service/updateservice.html'

    def get(self,request):
        data=request.get_full_path()
        data=data[-14:]
        singser=ServiceModel.objects.filter(serviceid=data).first()
        values={'nameofservice':singser.nameofservice,'typeofservice':singser.typeofservice,'startdate':singser.startdate,
                'description':singser.description,'seraddr':singser.seraddr,'servicemail':singser.servicemail,
                'servicephone':singser.servicephone,'websiteurl':singser.websiteurl,
                'serviceid':data}
        request.session.set_expiry(86400)
        request.session['serupd']=True
        request.session['serid']=data
        request.session['ownerid']=singser.owneremail
        request.session['sertype']=singser.typeofservice
        form_user=UpdateServiceForm(values)
        return render(request,self.template_name,{'singser':singser,'form_user':form_user})


    def post(self,request):
        form_user=UpdateServiceForm(request.POST)
        if form_user.is_valid():
            if request.session.get('serupd',None)==True and request.session['serid']!=None:
                serobj=ServiceModel.objects.filter(serviceid=request.session['serid']).first()
                serobj.nameofservice=form_user.cleaned_data.get('nameofservice')
                temp=form_user.cleaned_data.get('typeofservice')
                #ind=ChoiceModel.objects.get(iden=temp)
                serobj.startdate=form_user.cleaned_data.get('startdate')
                #print('iden',iden)
                serobj.typeofservice=temp
                serobj.servicemail=form_user.cleaned_data.get('servicemail')
                serobj.servicephone=form_user.cleaned_data.get('servicephone')
                serobj.websiteurl=form_user.cleaned_data.get('websiteurl')
                serobj.seraddr=form_user.cleaned_data.get('seraddr')
                serobj.description=form_user.cleaned_data.get('description')
                serobj.save()
                return redirect('/yourservices')
            else:
                return render(request,'home/error.html',{'main_error':'Logged out of session'})
        else:
            return render(request,'home/error.html',{'main_error':'Errors in form input','form':form_user})

class ReadMore(View):
    template_name='service/readmore.html'

    def get(self,request):
        data=request.get_full_path()
        data=data[-14:]
        values=ServiceModel.objects.filter(serviceid=data).first()
        temp=values.typeofservice
        #ind=ChoiceModel.objects.get(iden=temp).sertype
        singser={'nameofservice':values.nameofservice,'typeofservice':temp,'startdate':values.startdate,
                'description':values.description,'seraddr':values.seraddr,'servicemail':values.servicemail,
                'servicephone':values.servicephone,'websiteurl':values.websiteurl,
                'reviewcount':values.reviewcount,'avgrating':values.avgrating,
                'owneremail':values.owneremail}
        request.session.set_expiry(7202)
        user=request.session.get('uemail',None)
        if user!=None and user==values.owneremail:
            request.session['noquery']=True
        else:
            request.session['noquery']=False
            request.session['serupd']=True
            request.session['serid']=data
            request.session['ownerid']=values.owneremail
            request.session['sertype']=temp
        revobj=ReviewRate.objects.filter(serviceid=data).all()
        c=0
        i=0
        for rv in revobj:
            c+=rv.rating
            i=i+1
        avg=c/i
        revs=revobj[:3]
        return render(request,self.template_name,{'singser':singser,'revobjs':revs,'rating':avg})


class Filter(View):
    template_name='service/allservices.html'

    def get(self,request):
        data=int(request.get_full_path().split('/')[-1])
        ch=ChoiceModel.objects.get(iden=data).sertype
        serobj=ServiceModel.objects.filter(typeofservice=ch).all()
        return render(request,self.template_name,{'serobj':serobj,'filter':ch})

class MoreReview(View):
    template_name='service/morereviews.html'

    def get(self,request):
        data=request.get_full_path()
        data=data[-14:]
        revobjs=ReviewRate.objects.filter(serviceid=data).all()
        return render(request,self.template_name,{'revobjs':revobjs})

def submitreview(request):
    usermail=request.session.get("uemail",None)
    serid=request.session.get("serid",None)
    if request.method=="POST":
        if usermail==None or serid==None:
            return render(request,'home/error.html',{'main_error':'User has logged out'})
        rating=request.POST['rating']
        review=request.POST['review']
        revobj=ReviewRate(serviceid=serid,usermail=usermail,rating=rating,review=review)
        revobj.save()
        url='/readmore/id='+serid
        return redirect(url)

