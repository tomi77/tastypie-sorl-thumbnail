==============================
django-tastypie-sorl-thumbnail
==============================

.. image:: https://codeclimate.com/github/tomi77/tastypie-sorl-thumbnail/badges/gpa.svg
   :target: https://codeclimate.com/github/tomi77/tastypie-sorl-thumbnail
   :alt: Code Climate

Installation
============

Install package via ``pip``
::

    pip install django-tastypie-sorl-thumbnail

Usage
=====

::

   from tastypie.authentication import ApiKeyAuthentication
   from tastypie.authorization import DjangoAuthorization
   from tastypie.fields import FileField
   from tastypie.resources import ModelResource
   from tastypie_sorl_thumbnail.fields import ThumbnailField

   from test.models import Photo


   class VehiclePhotoResource(ModelResource):
       photo = FileField('photo')
       thumbnail = ThumbnailField('photo', '120', quality=80)

       class Meta:
           queryset = Photo.objects.all()
           resource_name = 'photo'
           authentication = ApiKeyAuthentication()
           authorization = DjangoAuthorization()
