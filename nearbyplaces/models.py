from django.db import models
from datetime import datetime

from placetype.models import PlaceType

class NearbyPlaces(models.Model):
    place_type = models.ForeignKey(PlaceType, on_delete=models.DO_NOTHING) 
    title = models.CharField(max_length=200)
    location_name = models.CharField(max_length=200)
    distance = models.DecimalField(max_digits=5, decimal_places=1)
    add_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title