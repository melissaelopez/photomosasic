from django import forms

from .models import Mosaic

class MosaicForm(forms.ModelForm):

    class Meta:
        model = Mosaic
        fields = ('title', 'text',)

class UploadPhotoForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
