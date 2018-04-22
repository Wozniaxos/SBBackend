from django.db import models
from .Instrument import Instrument
from .Artist import Artist

class ArtistInstrument(models.Model):
    type = models.CharField(max_length=30, null=True)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self