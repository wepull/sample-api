# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.err import Err  # noqa: E501
from swagger_server.models.get_auth_token_response import GetAuthTokenResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAuthenticationController(BaseTestCase):
    """AuthenticationController integration test stubs"""

    def test_auth_token(self):
        """Test case for auth_token

        AuthToken
        """
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example')]
        response = self.client.open(
            '/smt/authToken',
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
