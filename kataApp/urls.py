from django.conf.urls import  url

from kataApp import views

urlpatterns=[
    url(r'^$', views.index, name='index')

]
