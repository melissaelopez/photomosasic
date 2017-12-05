from django import forms

from .models import Mosaic
from .models import Photo

class MosaicForm(forms.Form):
    title = forms.CharField(max_length=50)
    source_image = forms.ImageField()

class UploadPhotoForm(forms.Form):
    class Meta:
        model = Photo
        fields = ('title', 'photo',)
