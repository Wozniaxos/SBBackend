from django.db import models

class Track(models.Model):
    url = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self