import factory
from . import models


class InstrumentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Instrument


class EventKindFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.EventKind


class MusicTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.MusicType


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Event


class BandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Band


class PhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Photo


class VideoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Video


class TrackFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Track


class ArtistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Artist


class ArtistInstrumentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ArtistInstrument
