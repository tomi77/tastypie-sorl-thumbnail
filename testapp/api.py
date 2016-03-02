from __future__ import absolute_import

from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie_sorl_thumbnail.fields import ThumbnailField

from .models import Photo


class PhotoResource(ModelResource):
    thumbnail = ThumbnailField('image', '120', quality=80)

    class Meta(object):
        queryset = Photo.objects.all()
        resource_name = 'photo'
        authentication = Authentication()
        authorization = Authorization()
