from django.conf.urls import include,url
from . import views
app_name='service'
urlpatterns=[
        url('',views.submitreview,name='review')
        ]
