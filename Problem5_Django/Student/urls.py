from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns= [

    url('',views.index,name='index'),
    url('',views.success,name='success'),

]