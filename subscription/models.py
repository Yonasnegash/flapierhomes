from django.db import models

from datetime import datetime

class Subscription(models.Model):
    email = models.CharField(max_length=100)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.email
