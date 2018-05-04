import factory
from . import models

class InstrumentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Instrument

class EventKindFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.EventKind

class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Event
