from django.db import models
from .MusicType import MusicType
from .EventKind import EventKind
from .Video import Video
from .Track import Track
from .Photo import Photo
from .Event import Event


class Band(models.Model):
    name = models.CharField(max_length = 30, null=True)
    city = models.CharField(max_length = 30, null=True)
    available_over_sea = models.BooleanField(default = False)
    willing_play_in_another_configuration = models.BooleanField(default = False)
    perform_radius = models.IntegerField(null=True)
    music_types = models.ManyToManyField(MusicType)
    minimum_hour_rate = models.IntegerField(null=True)
    preferred_events = models.ManyToManyField(EventKind)
    videos = models.ManyToManyField(Video)
    tracks = models.ManyToManyField(Track)
    photos = models.ManyToManyField(Photo)
    artists = models.ManyToManyField('Artist')
    events = models.ManyToManyField(Event)

    def __str__(self):
        return self.name