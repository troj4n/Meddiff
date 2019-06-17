from django.conf.urls import url
from django.conf.urls import include

from . import views
from django.conf import settings
from django.views.generic.base import RedirectView
from django.conf import settings

from django.conf.urls.static import static

from django.views.generic.base import RedirectView

from django.shortcuts import redirect
urlpatterns= [

    url(r'^$',views.get,name='get'),
    url(r'^insert/',views.insert,name='insert'),
    url(r'^display/',views.display,name='display'),
    url(r'^delete/',views.delete,name='delete'),
    url(r'^search/',views.search,name='search'),

]