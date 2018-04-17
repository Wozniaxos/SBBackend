from django.db import models

class MusicType(models.Model):
    def __str__(self):
        return self

class EventKind(models.Model):
    def __str__(self):
        return self

class Video(models.Model):
    def __str__(self):
        return self

class Track(models.Model):
    def __str__(self):
        return self

class Photo(models.Model):
    def __str__(self):
        return self

class Artist(models.Model):
    def __str__(self):
        return self

class Event(models.Model):
    def __str__(self):
        return self


class Band(models.Model):
    name = models.CharField(max_length = 30)
    city = models.CharField(max_length = 30)
    available_over_sea = models.BooleanField(default = False)
    willing_play_in_another_band = models.BooleanField(default = False)
    perform_radius = models.IntegerField()
    music_types = models.ManyToManyField(MusicType)
    minimum_hour_rate = models.IntegerField()
    preferred_events = models.ManyToManyField(EventKind)
    videos = models.ManyToManyField(Video)
    tracks = models.ManyToManyField(Track)
    photos = models.ManyToManyField(Photo)
    artists = models.ManyToManyField(Artist)
    events = models.ManyToManyField(Event)

    def __str__(self):
        return self.name



