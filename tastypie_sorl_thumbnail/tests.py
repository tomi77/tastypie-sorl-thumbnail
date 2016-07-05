import json

import six
from django.conf import settings
from tastypie.test import ResourceTestCase
from sorl.thumbnail.images import ImageFile
try:
    from unittest import mock
except ImportError:
    from mock import mock


class ThumbnailFieldTestCase(ResourceTestCase):
    fixtures = ['photo.yaml']

    @mock.patch('tastypie_sorl_thumbnail.fields.get_thumbnail')
    def test_with_image(self, mock_get_thumbnail):
        mock_get_thumbnail.side_effect = lambda path, *args, **kwargs: ImageFile('cache/%s' % path[len(settings.MEDIA_ROOT):])

        response = self.api_client.get('/v1/photo/1/')
        self.assertValidJSONResponse(response)
        content = response.content.decode('utf-8') if six.PY3 else response.content
        content = json.loads(content)
        self.assertEqual(content, {
            'id': 1,
            'image': 'http://example.com/media/image.png',
            'resource_uri': '/v1/photo/1/',
            'thumbnail': 'http://example.com/media/cache/image.png'
        })

    @mock.patch('tastypie_sorl_thumbnail.fields.get_thumbnail')
    def test_without_image(self, mock_get_thumbnail):
        mock_get_thumbnail.side_effect = Exception()

        response = self.api_client.get('/v1/photo/2/')
        self.assertValidJSONResponse(response)
        content = response.content.decode('utf-8') if six.PY3 else response.content
        content = json.loads(content)
        self.assertEqual(content, {
            'id': 2,
            'image': None,
            'resource_uri': '/v1/photo/2/',
            'thumbnail': None
        })
