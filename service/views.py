from django.shortcuts import render,redirect
from .models import Service as ServiceModel
from .models import Choice as ChoiceModel
from .forms import ServiceForm,UpdateServiceForm
from django.views.generic import View
import time,datetime
from django.http import HttpResponseRedirect
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
                'servicephone':singser.servicephone,'websiteurl':singser.websiteurl}
        request.session.set_expiry(3600)
        request.session['serupd']=True
        request.session['serid']=data
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
        ind=ChoiceModel.objects.get(iden=temp).sertype
        singser={'nameofservice':values.nameofservice,'typeofservice':ind,'startdate':values.startdate,
                'description':values.description,'seraddr':values.seraddr,'servicemail':values.servicemail,
                'servicephone':values.servicephone,'websiteurl':values.websiteurl,
                'reviewcount':values.reviewcount,'avgrating':values.avgrating,
                'owneremail':values.owneremail}
        request.session.set_expiry(3600)
        request.session['serupd']=True
        request.session['serid']=data
        return render(request,self.template_name,{'singser':singser})


