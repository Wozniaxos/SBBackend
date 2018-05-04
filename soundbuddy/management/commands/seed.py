from django.core.management.base import BaseCommand
from soundbuddy.factories import *
import factory
import random
from soundbuddy.models import *

class Command(BaseCommand):
    help = 'Seeds the database'

    def create_instruments(self):
        instruments = ['Guitar', 'Drums', 'Piano', 'Bass', 'Violin', 'Vocal']
        types = ['Main', 'Additional']
        for index in range(0, len(instruments)):
            InstrumentFactory.create(name = instruments[index], type = random.choice(types))

    def create_event_kinds(self):
        kinds = ['Wedding', 'Banquet', 'Concert', 'Cutlet', 'Birthday', 'Private Party']
        for index in range(0, len(kinds)):
            EventKindFactory.create(name = kinds[index])
        return EventKind.objects.all()

    def create_events(self, kinds):
        types = ['Private', 'Sound-Buddy']
        for index in range(40):
            EventFactory.create(
                type = random.choice(types),
                address = factory.Faker('address'),
                date = factory.Faker('date'),
                kind = random.choice(kinds),
                time = random.choice([60, 120, 240, 480]),
                salary = random.choice([30, 60, 90, 120, 200]),
                special_requirements = factory.Faker('sentence', nb_words=10)
            )

    def handle(self, *args, **options):
        Command.create_instruments(self)
        event_kinds = Command.create_event_kinds(self)
        events = Command.create_events(self, event_kinds)