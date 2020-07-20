# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.generator import Generator  # noqa: E501
from swagger_server.models.graph import Graph  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGeneratorsController(BaseTestCase):
    """GeneratorsController integration test stubs"""

    def test_generate(self):
        """Test case for generate

        Generate certain graph
        """
        body = Generator()
        response = self.client.open(
            '/api/graph/generate',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_generators(self):
        """Test case for get_generators

        Returns supported NetworkX generators
        """
        response = self.client.open(
            '/api/graph/generators',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
