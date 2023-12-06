# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.deeplink import Deeplink  # noqa: E501
from swagger_server.models.deeplinkresponse import Deeplinkresponse  # noqa: E501
from swagger_server.models.err import Err  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDeeplinkController(BaseTestCase):
    """DeeplinkController integration test stubs"""

    def test_get_deeplink(self):
        """Test case for get_deeplink

        to fetch the deeplink
        """
        body = Deeplink()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('account_id', 'account_id_example'),
                   ('tenant_id', 'tenant_id_example'),
                   ('authorization', 'authorization_example'),
                   ('environment', 'environment_example'),
                   ('channel', 'channel_example')]
        response = self.client.open(
            '/smt/deeplink',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
