from __future__ import unicode_literals

import os

from django.conf import settings
from sorl.thumbnail import get_thumbnail
from tastypie.fields import FileField

try:
    from tastypie import VERSION
except ImportError:
    from tastypie import __version__ as VERSION


class ThumbnailField(FileField):
    """
    A image thumbnail field.
    """
    dehydrated_type = 'string'
    help_text = 'A image thumbnail URL as a string. Ex: ' \
                '"http://media.example.com/media/photos/my_photo.jpg"'

    def __init__(self, attribute, geometry_string, null=False, help_text=None,
                 use_in='all', verbose_name=None, **sorl_options):
        field_options = dict(attribute=attribute, null=null, readonly=True,
                             help_text=help_text, use_in=use_in)
        if VERSION[:2] >= (0, 13):
            field_options.update({'verbose_name': verbose_name})
        super(ThumbnailField, self).__init__(**field_options)
        self.geometry_string = geometry_string
        self.sorl_options = sorl_options

    def convert(self, value):
        value = super(ThumbnailField, self).convert(value)

        if value is None:
            return None

        if value.startswith(settings.MEDIA_URL):
            value = value[len(settings.MEDIA_URL):]

        media_root = settings.MEDIA_ROOT \
            if settings.MEDIA_ROOT[-1] != os.path.sep \
            else settings.MEDIA_ROOT[:-1]
        image_path = '%s%s%s' % (media_root, os.path.sep, value)

        try:
            thumbnail = get_thumbnail(image_path, self.geometry_string,
                                      **self.sorl_options)
        except Exception:
            return None
        else:
            return thumbnail.url
