from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='root'),
    url(r'eventform', views.eventform, name='eventform'),
    url(r'eventlist', views.eventlist, name='eventlist'),
    url(r'map', views.map, name='map'),
    url(r'home', views.home, name='home'),
]