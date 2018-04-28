import factory
from . import models

class InstrumentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Instrument

    name = 'Guitar'
    type = 'Main'