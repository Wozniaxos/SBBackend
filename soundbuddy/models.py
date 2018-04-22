from django.db import models

class MusicType(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self

class Video(models.Model):
    url = models.CharField(max_length=30)
    def __str__(self):
        return self

class Track(models.Model):
    url = models.CharField(max_length=30)
    def __str__(self):
        return self

class Photo(models.Model):
    url = models.CharField(max_length=30)
    def __str__(self):
        return self

class Event(models.Model):
    type = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    date = models.DateField()
    kind = models.CharField(max_length=30)
    time = models.IntegerField()
    salary = models.IntegerField()
    special_requirements = models.CharField(max_length=300)
    def __str__(self):
        return self

class Instrument(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    def __str__(self):
        return self

class Artist(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    main_instrument = models.ForeignKey(Instrument)
    instruments = models.ManyToManyField(Instrument)
    bands = models.ManyToManyField(Band)

    def __str__(self):
        return self

class Band(models.Model):
    name = models.CharField(max_length = 30)
    city = models.CharField(max_length = 30)
    available_over_sea = models.BooleanField(default = False)
    willing_play_in_another_configuration = models.BooleanField(default = False)
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



