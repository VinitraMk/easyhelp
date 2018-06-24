from django.shortcuts import render
from django.views.generic import View
# Create your views here.
def index(request):
    return render(request,'home/cover.html',context={})

class About(View):
    template_name='home/about.html'

    def get(self,request):
        return render(request,self.template_name,{})

class Error(View):
    template_name='home/error.html'

    def get(self,request):
        return render(request,self.template_name,{})
