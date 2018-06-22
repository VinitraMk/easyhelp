from django.conf.urls import url 

from . import views
from django.conf import settings
'''app_name='login'

urlpatterns = [
            url('^$', views.login, name='login'),
            #url('^register/',views.register,name='register'),
            ]'''

if not settings.DEBUG:
    urlpatterns=patterns('',
                    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
                        )

