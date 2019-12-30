from django.db import models

# Create your models here.
class Flight(models.Model):
    flight_origin = models.CharField(max_length=50)
    flight_destination = models.CharField(max_length=50)
    flight_duration = models.IntegerField()
 
    def __str__(self):
        return (self.flight_origin)