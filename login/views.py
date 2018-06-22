from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View
from .models import User as UserModel
from .forms import UserForm
import requests
# Create your views here.

class Users(View):
    template_name='login/users.html'

    def get(self,request):
        user_list=[]
        form_user=UserForm()
        users=UserModel.objects.all()[:50]

        for user in users:
            user_list.append({'email':user.email,'password':user.password})

        return render(request,self.template_name, {
            'title':'Users List',
            'user_list':user_list,
            'form_user':form_user
            }
            )

    def post(self,request):
        form_user=UserForm(request.POST)
        if form_user.is_valid():
            form_user.save()
            return HttpResponseRedirect('/login/')


def index(request):
        r = requests.get('http://httpbin.org/status/418')
        print(r.text)
        return HttpResponse('<pre>' + r.text + '</pre>')
