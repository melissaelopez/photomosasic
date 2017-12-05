from django.db import models
from django.utils import timezone

from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/media/photos')

class Mosaic(models.Model):
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(storage=fs)
    upload_date = models.DateTimeField(auto_now_add=True)
