from django.core.management.base import BaseCommand
from soundbuddy.models import *


class Command(BaseCommand):
    help = 'Clear the database'

    def handle(self, *args, **options):
        Instrument.objects.all().delete()
        EventKind.objects.all().delete()
        Event.objects.all().delete()
        MusicType.objects.all().delete()
        Band.objects.all().delete()
        Photo.objects.all().delete()
        Track.objects.all().delete()
        Video.objects.all().delete()
        Artist.objects.all().delete()
        ArtistInstrument.objects.all().delete()
