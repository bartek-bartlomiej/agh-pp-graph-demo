# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.arrangment_info import ArrangmentInfo  # noqa: E501
from swagger_server.models.layout import Layout  # noqa: E501
from swagger_server.models.node_position import NodePosition  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAlgorithmsController(BaseTestCase):
    """AlgorithmsController integration test stubs"""

    def test_arrange(self):
        """Test case for arrange

        Arrange graph
        """
        body = ArrangmentInfo()
        response = self.client.open(
            '/api/graph/arrange',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_algorithms(self):
        """Test case for get_algorithms

        Returns supported NetworkX layout algorithms
        """
        response = self.client.open(
            '/api/graph/algorithms',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
