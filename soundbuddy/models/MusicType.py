from django.db import models

class MusicType(models.Model):
    name = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self