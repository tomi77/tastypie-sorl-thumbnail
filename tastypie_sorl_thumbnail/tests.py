import json

import six
from tastypie.test import ResourceTestCase
try:
    from unittest import mock
except ImportError:
    from mock import mock


class ThumbnailFieldTestCase(ResourceTestCase):
    fixtures = ['photo.yaml']

    @mock.patch('tastypie_sorl_thumbnail.fields.get_thumbnail')
    def test_with_image(self, mock_get_thumbnail):
        mock_get_thumbnail.return_value = 'cache/image.png'

        response = self.api_client.get('/v1/photo/1/')
        self.assertValidJSONResponse(response)
        content = response.content.decode('utf-8') if six.PY3 else response.content
        content = json.loads(content)
        self.assertEqual(content, {
            'id': 1,
            'image': '/media/image.png',
            'resource_uri': '/v1/photo/1/',
            'thumbnail': '/media/cache/image.png'
        })

    @mock.patch('tastypie_sorl_thumbnail.fields.get_thumbnail')
    def test_without_image(self, mock_get_thumbnail):
        mock_get_thumbnail.return_value = None

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
