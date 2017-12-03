from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.start, name='start'),
    url(r'^mosaic/(?P<pk>\d+)/$', views.mosaic_detail, name='mosaic_detail'),
    url(r'^mosaic/new/$', views.mosaic_new, name='mosaic_new'),
    url(r'^photo/new/$', views.photo_new, name='photo_new'),
]
