from django.core.management.base import BaseCommand
from soundbuddy.factories import *
import factory
import random
from soundbuddy.models import *


class Command(BaseCommand):
    help = 'Seeds the database'

    def create_instruments(self):
        instruments = ['Guitar', 'Drums', 'Piano', 'Bass', 'Violin', 'Vocal']
        for index in range(0, len(instruments)):
            InstrumentFactory.create(name=instruments[index])
        return Instrument.objects.all()

    def create_music_types(self):
        types = ['Rock', 'Disco-Polo', 'Pop', 'Jazz', 'Soul', 'Rnb']
        for index in range(0, len(types)):
            MusicTypeFactory.create(name=types[index])
        return MusicType.objects.all()

    def create_event_kinds(self):
        kinds = ['Wedding', 'Banquet', 'Concert',
                 'Cutlet', 'Birthday', 'Private Party']
        for index in range(0, len(kinds)):
            EventKindFactory.create(name=kinds[index])
        return EventKind.objects.all()

    def create_events(self, kinds):
        types = ['Private', 'Sound-Buddy']
        for index in range(200):
            EventFactory.create(
                type=random.choice(types),
                address=factory.Faker('address'),
                date=factory.Faker('date'),
                kind=random.choice(kinds),
                time=random.choice([60, 120, 240, 480]),
                salary=random.choice([30, 60, 90, 120, 200]),
                special_requirements=factory.Faker('sentence', nb_words=10)
            )
        return Event.objects.all()

    def create_bands(self, music_types, events, event_kinds):
        for index in range(70):
            music_types_for_band = []
            events_for_band = []
            preferred_events = []
            for x in range(3):
                type = random.choice(music_types)
                event_for_band = random.choice(events)
                kind = random.choice(event_kinds)
                music_types_for_band.append(type)
                events_for_band.append(event_for_band)
                preferred_events.append(kind)
            band = BandFactory.create(
                name=factory.Faker('company'),
                city=factory.Faker('city'),
                available_over_sea=factory.Faker('boolean'),
                willing_play_in_another_configuration=factory.Faker('boolean'),
                perform_radius=random.choice([30, 100, 200, 500, 1000]),
                minimum_hour_rate=random.choice([30, 60, 90, 120, 150, 200]),
            )
            band.music_types.set(music_types_for_band)
            band.events.set(events_for_band)
            band.preferred_events.set(preferred_events)
        return Band.objects.all()

    def create_media(self, bands):
        for x in range(0, 1000):
            PhotoFactory.create(
                url=factory.Faker('image_url'),
                band=random.choice(bands)
            )

        for index in range(0, len(bands)):
            VideoFactory.create(
                url='https://www.youtube.com/watch?v=QBuZ6kRHLuI',
                band=bands[index]
            )
            TrackFactory.create(
                url='https://soundcloud.com/famous_dex1/japan',
                band=bands[index]
            )

    def create_artists(self, bands):
        for index in range(0, len(bands)):
            artist = ArtistFactory.create(
                name=factory.Faker('name'),
                city=factory.Faker('city'),
            )
            band = bands[index]
            artist.bands.add(band)
        for index in range(100):
            artist = ArtistFactory.create(
                name=factory.Faker('name'),
                city=factory.Faker('city'),
            )
            band = random.choice(bands)
            artist.bands.add(band)
        return Artist.objects.all()

    def create_artists_instrument(self, artists, instruments):
        for index in range(0, len(artists)):
            ArtistInstrumentFactory.create(
                type=random.choice(['Main', 'Additional']),
                instrument=random.choice(instruments),
                artist=artists[index]
            )

    def handle(self, *args, **options):
        instruments = Command.create_instruments(self)
        event_kinds = Command.create_event_kinds(self)
        events = Command.create_events(self, event_kinds)
        music_types = Command.create_music_types(self)
        bands = Command.create_bands(self, music_types, events, event_kinds)
        Command.create_media(self, bands)
        artists = Command.create_artists(self, bands)
        Command.create_artists_instrument(self, artists, instruments)
