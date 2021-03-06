from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.leaflet, name='root'),
    url(r'eventform', views.eventform, name='eventform'),
    url(r'eventlist', views.eventlist, name='eventlist'),
    url(r'map', views.map, name='map'),
    url(r'home', views.home, name='home'),
    url(r'logo', views.logo, name='logo'),  #remove when done testing
    url(r'mapbox',views.mapbox, name='mapbox'), #remove when done testing
    url(r'leaflet',views.leaflet, name='leaflet'),
    url(r'friday',views.friday, name='friday'),
    url(r'saturday',views.saturday, name='saturday'),
    url(r'sunday',views.sunday, name='sunday'),
    url(r'filter/(?P<weekday>\d+)/$',views.filter, name='filter')
]