from django.conf.urls import url

from . import views
app_name='login'
urlpatterns=[
        url('^$',views.index,name='index'),
        ]
