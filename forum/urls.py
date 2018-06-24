from django.conf.urls import include,url
app_name='forum'
from . import views
urlpatterns=[
        url('',views.query,name='query'),
        ]
