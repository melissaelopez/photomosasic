from django import forms

from .models import Mosaic
from .models import Photo

class MosaicForm(forms.ModelForm):

    class Meta:
        model = Mosaic
        fields = ('title', 'text',)

class UploadPhotoForm(forms.Form):
    class Meta:
        model = Photo
        fields = ('title', 'photo',)
