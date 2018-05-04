from django.db import models

class Instrument(models.Model):
    name = models.CharField(max_length=30, null=True)
    type = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.name

class EventKind(models.Model):
    name = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.name

class Event(models.Model):
    type = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=100, null=True)
    date = models.DateField(null=True)
    kind = models.ForeignKey(EventKind, on_delete=models.CASCADE, null=True)
    time = models.IntegerField(null=True)
    salary = models.IntegerField(null=True)
    special_requirements = models.CharField(max_length=300, null=True)
    def __str__(self):
        return self.kind.name

class MusicType(models.Model):
    name = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.name

class Band(models.Model):
    name = models.CharField(max_length = 30, null=True)
    city = models.CharField(max_length = 30, null=True)
    available_over_sea = models.BooleanField(default = False)
    willing_play_in_another_configuration = models.BooleanField(default = False)
    perform_radius = models.IntegerField(null=True)
    music_types = models.ManyToManyField(MusicType)
    minimum_hour_rate = models.IntegerField(null=True)
    preferred_events = models.ManyToManyField(EventKind)
    events = models.ManyToManyField(Event)

    def __str__(self):
        return self.name

class Photo(models.Model):
    url = models.CharField(max_length=30, null=True)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.url

class Track(models.Model):
    url = models.CharField(max_length=30, null=True)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.url

class Video(models.Model):
    url = models.CharField(max_length=30, null=True)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.url

class Artist(models.Model):
    name = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=30, null=True)
    bands = models.ManyToManyField(Band)

    def __str__(self):
        return self.name

class ArtistInstrument(models.Model):
    type = models.CharField(max_length=30, null=True)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.type