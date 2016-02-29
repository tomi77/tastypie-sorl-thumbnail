Quick Start
===========

Install package via ``pip``
::

    pip install django-tastypie-sorl-thumbnail

Simple usage
::

   from tastypie.authentication import ApiKeyAuthentication
   from tastypie.authorization import DjangoAuthorization
   from tastypie.fields import FileField
   from tastypie.resources import ModelResource
   from tastypie_sorl_thumbnail.fields import ThumbnailField

   from test.models import Photo


   class PhotoResource(ModelResource):
       photo = FileField('photo')
       thumbnail = ThumbnailField('photo', '120', quality=80)

       class Meta(object):
           queryset = Photo.objects.all()
           resource_name = 'photo'
           authentication = ApiKeyAuthentication()
           authorization = DjangoAuthorization()
