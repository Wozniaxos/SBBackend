from django.test import TestCase
from soundbuddy.models import Video

class VideoTest(TestCase):

    def create_video(self, url='this is the url'):
        return Video.objects.create(url=url)

    def test_whatever_creation(self):
        w = self.create_video()
        self.assertTrue(isinstance(w, Video))
        self.assertEqual(w.url, 'this is the url')