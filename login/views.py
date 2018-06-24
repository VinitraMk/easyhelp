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
                #print('Existing user',existing_user.name)
                request.session.set_expiry(86400)
                request.session['logged']=True
                request.session['uname']=existing_user.name
                request.session['uemail']=existing_user.email
                return redirect('/')
            else:
                form_user=UserForm()
                #request.session['error']='Invalid username or password'
                return render(request,self.template_name,{'form_user':form_user,'error':'User does not exist!'})


class Logout(View):
    def get(self,request):
        request.session['logged']=False
        return redirect('/')



class Profile(View):
    template_name='login/index.html'
    def get(self,request):
        email=request.session['uemail']
        existing_user=UserModel.objects.get(email=email)
        return render(request,self.template_name,{'user_name':existing_user.name,'user_email':existing_user.email})
    
