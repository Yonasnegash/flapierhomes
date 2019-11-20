from django.db import models
from datetime import datetime

class HomeType(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    register_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
