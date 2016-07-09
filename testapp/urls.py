from django import VERSION
from django.conf.urls import include, url
from tastypie.api import Api

from .api import PhotoResource


api = Api(api_name='v1')
api.register(PhotoResource())

if VERSION[:2] >= (1, 7):
    urlpatterns = [
        url(r'^', include(api.urls))
    ]
else:
    from django.conf.urls import patterns

    urlpatterns = patterns('', url(r'^', include(api.urls)))
