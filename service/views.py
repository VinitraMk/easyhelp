from django.shortcuts import render,redirect
from .models import Service 
from .forms import ServiceForm
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
            st=datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
            print('st',st)
            user=form_user.save(commit=False)
            user.serviceid=st
            user.owneremail=request.session['uemail']
            print('st',user.owneremail,user.serviceid)
            user.save()
            return redirect('/profile')
        else:
            request.session['error']='form invalid'
            return render(request,'home/error.html',{'form':form_user})



