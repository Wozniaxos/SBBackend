from django.db import models

class Instrument(models.Model):
    name = models.CharField(max_length=30, null=True)
    type = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self