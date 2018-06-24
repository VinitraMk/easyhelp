from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class Forum(View):
    template_name='forum/forum.html'

    def get(self,request):
        return render(request,self.template_name,{})
