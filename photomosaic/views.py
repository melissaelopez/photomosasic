# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Mosaic
from .forms import MosaicForm
from .forms import UploadPhotoForm
from get_mosaic import make_mosaic
from PIL import Image

def start(request):
    mosaics = Mosaic.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'photomosaic/start.html', {'mosaics': mosaics})

def mosaic_detail(request, pk):
    mosaic = get_object_or_404(Mosaic, pk=pk)
    return render(request, 'photomosaic/mosaic_detail.html', {'mosaic': mosaic})

# def mosaic_new(request):
#     if request.method == "POST":
#         form = MosaicForm(request.POST)
#         if form.is_valid():
#             mosaic = form.save(commit=False)
#             mosaic.author = request.user
#             mosaic.published_date = timezone.now()
#             mosaic.save()
#
#             return redirect('mosaic_detail', pk=mosaic.pk)
#     else:
#         form = MosaicForm()
#     return render(request, 'photomosaic/mosaic_edit.html', {'form': form})

def handle_uploaded_file(f):
    mosaic = make_mosaic(f, (1000,1000), 10, 10, (100,100))

def mosaic_new(request):
    if request.method == "POST":
        form = MosaicForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            title = data['title']
            handle_uploaded_file(request.FILES['source_image'])
            mosaic=Mosaic.objects.create(title=title)
            return redirect('mosaic_detail', pk=mosaic.pk)
    else:
        form = MosaicForm()
    return render(request, 'photomosaic/mosaic_edit.html', {'form': form})

def photo_new(request):
    if request.method == 'POST':
        form = UploadPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            #handle_uploaded_file(request.FILES['file'])
            #using model forms to save images instead
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = UploadPhotoForm()
    return render(request, 'photomosaic/photo_edit.html', {'form': form})

def about(request):
    return render(request, 'photomosaic/about.html', {})
