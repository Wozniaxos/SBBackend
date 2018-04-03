from django.db import models


class Band(models.Model):
    name = models.CharField(default = 'Band', max_length = 30)
    def __str__(self):
        return self.name

class Musician(models.Model):
    name = models.CharField(default = 'Musician', max_length = 30)
    band = models.ForeignKey(Band, default = 0, on_delete = models.CASCADE)
    def __str__(self):
        return self.name


