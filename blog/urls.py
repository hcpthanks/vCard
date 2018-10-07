from django.urls import path
from . import views
from django.conf.urls import url 

app_name='blog'
urlpatterns = [
    path('', view=views.blog_list, name='blog_list'), 
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',  view=views.blog_detail, name='blog_detail'),
]  