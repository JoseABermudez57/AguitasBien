from django.db import models

# Create your models here.
class Watersample(models.Model):
    timestamp = models.DateTimeField()
    ph = models.FloatField()
    termo = models.FloatField()
    condu = models.FloatField()
    otroSensor = models.FloatField()
    
    def __str__(self):
        return self.name

class Modelprofile(models.Model):
    timestamp = models.DateTimeField()
    ph = models.FloatField()
    temperature = models.FloatField()
    conductivity = models.FloatField()

    def __str__(self):
        return self.name