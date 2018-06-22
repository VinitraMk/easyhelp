from django.shortcuts import render
from django.views.generic import View
# Create your views here.
def index(request):
    return render(request,'home/index.html',context={})

class About(View):
    template_name='home/about.html'

    def get(self,request):
        return render(request,self.template_name,{})
