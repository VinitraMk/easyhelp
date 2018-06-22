from django.conf.urls import url
from . import views
from django.conf import settings
app_name='home'
urlpatterns = [
            url(r'^$', views.index, name='index'),
            ]

if not settings.DEBUG:
    urlpatterns+=patterns('',
            (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
                )
