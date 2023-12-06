# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.err import Err  # noqa: E501
from swagger_server.models.secure_message_request import SecureMessageRequest  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSecureMessageController(BaseTestCase):
    """SecureMessageController integration test stubs"""

    def test_sendsecuremessage(self):
        """Test case for sendsecuremessage

        sendsecuremessage
        """
        body = SecureMessageRequest()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example')]
        response = self.client.open(
            '/smt/sendsecuremessage',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
