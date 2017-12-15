import os
import color_id
import logging
#import cloudstorage as gcs

import random, string

from django.db import models
from PIL import Image
from django.utils import timezone

#from django.core.files.storage import Storage
from django.core.files.storage import FileSystemStorage

#from google.appengine.api import app_identity
from google.cloud import storage
from google.cloud.storage import Blob

fs = FileSystemStorage(location=os.path.join('.', 'media', 'photos'))

class Mosaic(models.Model):
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(storage=fs)
    upload_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        #instantiate client
        storage_client = storage.Client()

        #access google cloud storage bucket
        bucket = storage_client.get_bucket('photomosaic_storage')

        #convert image to PIL object and classify it
        pil_image = Image.open(self.photo)
        color = color_id.get_classification('asdf', pil_image)

        #edit save file path to corresponding color folder
        new_path = 'media/photos/' + color[0] + '/' + self.photo.name

        #need to save before transferring
        super(Photo, self).save(*args, **kwargs)
        
        #upload photo to bucket
        blob = Blob(new_path, bucket)
        blob.upload_from_file(self.photo.file)





        
#         Below is the code for local storage (similar to the above)
##        #convert image to PIL object and classify it
##        pil_image = Image.open(self.photo)
##        color = color_id.get_classification('asdf', pil_image)
##
##        #edit save file path to corresponding color folder
##        new_path = self.photo.path[:-(len(self.photo.name)+1)]
##        new_path =  os.path.join(new_path, color[0])
##
##        #check if a folder exists for that color and create a new one if it doesn't
##        #race condition handling from:
##        #https://stackoverflow.com/questions/273192/how-can-i-create-a-directory-if-it-does-not-exist
##        if not os.path.exists(new_path):
##            try:
##                os.makedirs(new_path)
##            except OSError as e:
##                if exception.errno != errno.EEXIST:
##                        raise
##
##        test_path = os.path.join(new_path, self.photo.name)
##
##        #check if image exists already
##        while os.path.exists(test_path):
##            #generate a random string
##            #https://stackoverflow.com/questions/37675280/how-to-generate-a-random-string
##            random_string = ''.join(random.choice(string.ascii_letters) for i in range(7))
##            random_string = '_' + random_string
##
##            #split extension from image name
##            split = os.path.splitext(self.photo.name)
##
##            #generate a new path with the random string appended to image name
##            test_path = os.path.join(new_path, split[0] + random_string + split[1])
##
##        new_path = test_path
##        
##        #save the photo normally
##        super(Photo, self).save(*args, **kwargs)
##
##        #move the photo into the classified folder after saving it
##        if os.path.isfile(self.photo.path):
##            os.rename(self.photo.path, new_path)

        #different way of upload (not as good)
        #save the image locally and then transfer it to cloud storage
        #super(Photo, self).save(*args, **kwargs)      
        #image_path = os.path.join('.', 'media', 'photos', self.photo.name)
        #blob.upload_from_filename(image_path)
