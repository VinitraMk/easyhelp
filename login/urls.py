<<<<<<< HEAD
from django.conf.urls import url 

from . import views

'''app_name='login'

urlpatterns = [
            url('^$', views.login, name='login'),
            #url('^register/',views.register,name='register'),
            ]'''
=======
from django.conf.urls import url

from . import views
app_name='login'
urlpatterns=[
        url('^$',views.index,name='index'),
        ]
>>>>>>> 96dc01c13c27b2eb11515d77e0a8fadb689b928c
