#from django.db import models
from django.conf import settings
from django.contrib.gis.db import models
import googlemaps

gmaps = googlemaps.Client(key=settings.GOOGLEMAPSAPI)
# Create your models here.

EVENTTYPE_CHOICES = (('SF','Single Family'),
                     ('MF','Multi Family'),
                     ('ES','Estate Sale'),
                     ('CE','Church Event'),
                     ('SE','School Event'),
                     ('FM','Farm Market'),
                     ('FB','Food or Beverage Event'),
                     ('HE', 'Holiday Event'),
                     ('CS', 'Craft Show or Flea Market'))
STATE_CHOICES = (('DE','Delaware'),
                 ('MD','Maryland'),
                 ('PA','Pennsylvania'))

class Event(models.Model):
    eventType = models.CharField(max_length=2, choices = EVENTTYPE_CHOICES,default='SF')
    title = models.CharField(max_length=200)
    day = models.DateField(blank=True, null=True)
    start = models.TimeField(blank=True, null=True)
    end = models.TimeField(blank=True, null=True)
    street = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, choices=STATE_CHOICES, default='PA')
    description = models.CharField(max_length=1000)
    timestampAdded = models.DateTimeField()
    timestampUpdated = models.DateTimeField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    geojsonstring = models.TextField(default='{}')

    def __str__(self):
        return self.title