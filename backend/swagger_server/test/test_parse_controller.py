# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.graph import Graph  # noqa: E501
from swagger_server.test import BaseTestCase


class TestParseController(BaseTestCase):
    """ParseController integration test stubs"""

    def test_upload_file(self):
        """Test case for upload_file

        Parse graph from attached files
        """
        body = Object()
        response = self.client.open(
            '/api/graph/parse',
            method='POST',
            data=json.dumps(body),
            content_type='application/octet-stream')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
