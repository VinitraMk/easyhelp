"""easyhelp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include,url
import login.views as UserViews
import home.views as HomeViews
import service.views as ServiceViews
import forum.views as ForumViews
urlpatterns = [
    url('',include('home.urls')),
    url(r'^error',HomeViews.Error.as_view()),
    url(r'^logout',UserViews.Logout.as_view()),
    url(r'^about/',HomeViews.About.as_view()),
    url(r'^register/',UserViews.Register.as_view()),
    url(r'^login/',UserViews.Login.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^addservice/',ServiceViews.Service.as_view()),
    url(r'^profile/',UserViews.Profile.as_view()),
    url(r'^yourservices/',ServiceViews.YourServices.as_view()),
    url(r'^updateservice/',ServiceViews.ServiceInfo.as_view()),
    url(r'^updateservice/id=[0-9]+$',ServiceViews.ServiceInfo.as_view()),
    url(r'^allservices/',ServiceViews.AllServices.as_view()),
    url(r'^readmore/id=[0-9]+$',ServiceViews.ReadMore.as_view()),
    url(r'^forum/',ForumViews.Forum.as_view()),
    url(r'^filterser/[0-9]+$',ServiceViews.Filter.as_view()),
    url(r'^askquery/id=[0-9]+$',include('forum.urls',namespace='query')),
]

