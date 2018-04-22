from django.contrib import admin

from .models import MusicType, Video, Track, Photo, Event, Instrument, ArtistInstrument, Artist, Band

admin.site.register(MusicType)
admin.site.register(Video)
admin.site.register(Track)
admin.site.register(Photo)
admin.site.register(Event)
admin.site.register(Instrument)
admin.site.register(Artist)
admin.site.register(Band)
admin.site.register(ArtistInstrument)

