from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import View
from .models import User as UserModel
from .forms import UserForm,LoginForm
from django.contrib import messages 
from django.contrib.auth.hashers import make_password
from passlib.hash import pbkdf2_sha256


# Create your views here.

class Register(View):
    template_name='login/register.html'

    def get(self,request):
        form_user=UserForm()
        return render(request,self.template_name,{'form_user':form_user})

    def post(self,request):
        form_user=UserForm(request.POST)
        if form_user.is_valid():
            #form_user.save()
            existing_user=UserModel.objects.filter(email=form_user.cleaned_data.get('email')).first()
            if existing_user:
                context = {'form_user':form_user,'error':'A user with this email already exists'}
                return render(request,self.template_name,context)
            #return render(request,'home/index.html',{})
            user=form_user.save(commit=False)
            clearPass=form_user.cleaned_data['password']
            varhash=pbkdf2_sha256.hash(clearPass)
            user.password=varhash
            user.save()
            return redirect('/login')


class Login(View):
    template_name='login/login.html'
    redirect_template='home/index.html'

    def get(self,request):
        form_user=LoginForm()
        return render(request,self.template_name,{'form_user':form_user})

    def post(self,request):
        login_user=LoginForm(request.POST)
        if login_user.is_valid():
            uname=login_user.cleaned_data.get('email')
            pwd=login_user.cleaned_data.get('password')
            #existing_user=UserModel.objects.filter(email=login_user.cleaned_data.get('email')).first()
            existing_user=UserModel.objects.get(email=uname)
            if existing_user and pbkdf2_sha256.verify(pwd,existing_user.password):
                print('Existing user',existing_user.name)
                request.session.set_expiry(86400)
                request.session['logged']=True
                request.session['uname']=existing_user.name
                request.session['uemail']=existing_user.email
                return redirect('/')
            else:
                form_user=UserForm()
                #request.session['error']='Invalid username or password'
                return render(request,self.template_name,{'form_user':form_user,'error':'User does not exist!'})


=======
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
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
>>>>>>> 96dc01c13c27b2eb11515d77e0a8fadb689b928c
