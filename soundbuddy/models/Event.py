from django.db import models
from .EventKind import EventKind

class Event(models.Model):
    type = models.CharField(max_length=30, null=True)
    adress = models.CharField(max_length=30, null=True)
    date = models.DateField(null=True)
    kind = models.ForeignKey(EventKind, on_delete=models.CASCADE, null=True)
    time = models.IntegerField(null=True)
    salary = models.IntegerField(null=True)
    special_requirements = models.CharField(max_length=300, null=True)
    def __str__(self):
        return self