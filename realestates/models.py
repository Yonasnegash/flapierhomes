from django.db import models
from datetime import datetime

class RealEstate(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=200)
    agent = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)
    register_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
