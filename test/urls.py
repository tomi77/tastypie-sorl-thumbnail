from django.conf.urls import patterns, include, url
from tastypie.api import Api

from .api import PhotoResource


api = Api(api_name='v1')
api.register(PhotoResource())

urlpatterns = patterns('', url(r'^', include(api.urls)))
