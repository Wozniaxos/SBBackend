from django.test import TestCase
from soundbuddy.models import *


class InstrumentTest(TestCase):

    def create_instrument(self, name='Guitar', type='main'):
        return Instrument.objects.create(name=name, type=type)

    def test_instrument_creation(self):
        i = self.create_instrument()
        self.assertTrue(isinstance(i, Instrument))
        self.assertEqual(i.name, 'Guitar')
        self.assertEqual(i.type, 'main')


class EventTest(TestCase):

    def create_event_kind(self, name='Wedding'):
        return EventKind.objects.create(name=name)

    def test_event_kind_creation(self):
        e = self.create_event_kind()
        self.assertTrue(isinstance(e, EventKind))
        self.assertEqual(e.name, 'Wedding')

    def create_event(self, type='private',
                     address='street 1',
                     time=120,
                     salary=100,
                     special_requirements='special requirements'
                     ):
        event_kind = self.create_event_kind()
        return Event.objects.create(
            type=type,
            address=address,
            kind=event_kind,
            time=time,
            salary=salary,
            special_requirements=special_requirements
        )

    def test_event_creation_with_event_kind_relation(self):
        e = self.create_event()
        self.assertTrue(isinstance(e, Event))
        self.assertTrue(isinstance(e.kind, EventKind))
        self.assertEqual(e.type, 'private')
        self.assertEqual(e.address, 'street 1')
        self.assertEqual(e.time, 120)
        self.assertEqual(e.salary, 100)
        self.assertEqual(e.special_requirements, 'special requirements')
        self.assertEqual(e.kind.name, 'Wedding')


class MusicTypeTest(TestCase):

    def create_music_type(self, name='Jazz'):
        return MusicType.objects.create(name=name)

    def test_music_type_creation(self):
        m = self.create_music_type()
        self.assertTrue(isinstance(m, MusicType))
        self.assertTrue(m.name, 'Jazz')


class ExternalMedia(TestCase):

    def create_photo(self, url='this is the url'):
        return Photo.objects.create(url=url)

    def create_track(self, url='this is the url'):
        return Track.objects.create(url=url)

    def create_video(self, url='this is the url'):
        return Video.objects.create(url=url)

    def test_external_media_creation(self):
        v = self.create_video()
        t = self.create_track()
        p = self.create_photo()

        self.assertTrue(isinstance(v, Video))
        self.assertTrue(isinstance(t, Track))
        self.assertTrue(isinstance(p, Photo))
        self.assertEqual(v.url, 'this is the url')
        self.assertEqual(t.url, 'this is the url')
        self.assertEqual(p.url, 'this is the url')


class BandTest(TestCase):

    def create_band_with_relations(self, name='weselnicy', city='city'):
        band = Band.objects.create(name=name, city=city)
        Photo.objects.create(url='photo1url', band=band)
        Photo.objects.create(url='photo2url', band=band)
        Track.objects.create(url='track1url', band=band)
        Track.objects.create(url='track2url', band=band)
        Video.objects.create(url='video1url', band=band)
        Video.objects.create(url='video2url', band=band)
        music_type_1 = MusicType.objects.create(name='Jazz')
        music_type_2 = MusicType.objects.create(name='Sould')
        band.music_types.add(music_type_1)
        band.music_types.add(music_type_2)
        event_kind_1 = EventKind.objects.create(name='Wedding')
        event_kind_2 = EventKind.objects.create(name='Birthday')
        band.preferred_events.add(event_kind_1)
        band.preferred_events.add(event_kind_2)
        return band

    def test_band_creation_with_relations(self):
        b = self.create_band_with_relations()
        self.assertTrue(isinstance(b, Band))
        self.assertTrue(b.music_types.count, 2)
        self.assertTrue(b.preferred_events.count, 2)
        self.assertTrue(b.preferred_events.all()[0]
                        .band_set.all()[0].name, 'weselnicy')
        self.assertTrue(b.preferred_events.all()[1]
                        .band_set.all()[0].name, 'weselnicy')
        self.assertTrue(b.music_types.all()[0]
                        .band_set.all()[0].name, 'weselnicy')
        self.assertTrue(b.music_types.all()[1]
                        .band_set.all()[0].name, 'weselnicy')
        self.assertTrue(b.photo_set.all()[0].url, 'photo1url')
        self.assertTrue(b.photo_set.all()[1].url, 'photo2url')
        self.assertTrue(b.track_set.all()[0].url, 'track1url')
        self.assertTrue(b.track_set.all()[1].url, 'track2url')
        self.assertTrue(b.video_set.all()[0].url, 'video1url')
        self.assertTrue(b.video_set.all()[1].url, 'video2url')


class ArtistTest(TestCase):

    def create_artist_with_relations(self, name='Kacper', city='city'):
        artist = Artist.objects.create(name=name, city=city)
        band_1 = Band.objects.create(name='band1')
        band_2 = Band.objects.create(name='band2')
        artist.bands.add(band_1)
        artist.bands.add(band_2)
        instrument_1 = Instrument.objects.create(name='Guitar')
        instrument_2 = Instrument.objects.create(name='Piano')
        ArtistInstrument.objects.create(artist=artist, instrument=instrument_1)
        ArtistInstrument.objects.create(artist=artist, instrument=instrument_2)
        return artist

    def test_artist_creation_with_relations(self):
        a = self.create_artist_with_relations()
        self.assertTrue(isinstance(a, Artist))
        self.assertTrue(a.bands.count, 2)
        self.assertTrue(a.name, 'Kacper')
        self.assertTrue(a.city, 'city')
        self.assertTrue(a.artistinstrument_set.count, 2)
        self.assertTrue(a.artistinstrument_set.all()[0]
                        .instrument.name, 'Guitar')
        self.assertTrue(a.artistinstrument_set.all()[1]
                        .instrument.name, 'Piano')
        self.assertTrue(a.bands.all()[0].name, 'band1')
        self.assertTrue(a.bands.all()[1].name, 'band2')


class ArtistInstrumentTest(TestCase):

    def create_artist_instrument(self):
        artist = Artist.objects.create(name='Kacper')
        instrument = Instrument.objects.create(name='Guitar')
        return ArtistInstrument.objects.create(artist=artist,
                                               instrument=instrument
                                               )

    def test_artist_instrument_creation_with_relations(self):
        a = self.create_artist_instrument()
        self.assertTrue(isinstance(a, ArtistInstrument))
        self.assertTrue(isinstance(a.instrument, Instrument))
        self.assertTrue(isinstance(a.artist, Artist))
        self.assertTrue(a.instrument.name, 'Guitar')
        self.assertTrue(a.artist.name, 'Kacper')
