==============================
django-tastypie-sorl-thumbnail
==============================

.. image:: https://codeclimate.com/github/tomi77/tastypie-sorl-thumbnail/badges/gpa.svg
   :target: https://codeclimate.com/github/tomi77/tastypie-sorl-thumbnail
   :alt: Code Climate
.. image:: https://travis-ci.org/tomi77/tastypie-sorl-thumbnail.svg?branch=master
   :target: https://travis-ci.org/tomi77/tastypie-sorl-thumbnail
.. image:: https://coveralls.io/repos/github/tomi77/tastypie-sorl-thumbnail/badge.svg?branch=master
   :target: https://coveralls.io/github/tomi77/tastypie-sorl-thumbnail?branch=master

Add a ``sorl-thumbnail`` support for a Django Tastypie.

Installation
============

Install package via ``pip``
::

    pip install django-tastypie-sorl-thumbnail

Usage
=====

::

   from tastypie.authentication import Authentication
   from tastypie.authorization import Authorization
   from tastypie.resources import ModelResource
   from tastypie_sorl_thumbnail.fields import ThumbnailField

   from .models import Photo


   class PhotoResource(ModelResource):
       thumbnail = ThumbnailField('photo', '120', quality=80)

       class Meta(object):
           queryset = Photo.objects.all()
           resource_name = 'photo'
           authentication = Authentication()
           authorization = Authorization()
