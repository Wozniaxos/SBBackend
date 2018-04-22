from django.db import models
from .Band import Band

class Artist(models.Model):
    name = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=30, null=True)
    bands = models.ManyToManyField(Band)

    def __str__(self):
        return self