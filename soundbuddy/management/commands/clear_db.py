from django.core.management.base import BaseCommand
from soundbuddy.models import *


class Command(BaseCommand):
    help = 'Clear the database'

    def handle(self, *args, **options):
        Instrument.objects.all().delete()
        EventKind.objects.all().delete()
        Event.objects.all().delete()