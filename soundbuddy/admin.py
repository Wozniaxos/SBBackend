from django.contrib import admin

from .models.MusicType import MusicType
from .models.Video import Video
from .models.Track import Track
from .models.Photo import Photo
from .models.Event import Event
from .models.Instrument import Instrument
from .models.ArtistInstrument import ArtistInstrument
from .models.Artist import Artist
from .models.Band import Band

admin.site.register(MusicType)
admin.site.register(Video)
admin.site.register(Track)
admin.site.register(Photo)
admin.site.register(Event)
admin.site.register(Instrument)
admin.site.register(Artist)
admin.site.register(Band)
admin.site.register(ArtistInstrument)

