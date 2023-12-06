# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.err import Err  # noqa: E501
from swagger_server.models.existinguser import Existinguser  # noqa: E501
from swagger_server.models.newuser import Newuser  # noqa: E501
from swagger_server.models.newuserpinrules import Newuserpinrules  # noqa: E501
from swagger_server.test import BaseTestCase


class TestIVRAuthenticationController(BaseTestCase):
    """IVRAuthenticationController integration test stubs"""

    def test_validate_pin(self):
        """Test case for validate_pin

        to validate the pins entered by the new user
        """
        body = Newuser()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example')]
        response = self.client.open(
            '/smt/validatePIN',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_validate_pin_rules(self):
        """Test case for validate_pin_rules

        to validate if pin entered by new user follows pin rules
        """
        body = Newuserpinrules()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example')]
        response = self.client.open(
            '/smt/validatePINRules',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_validate_user(self):
        """Test case for validate_user

        to validate the exiting user
        """
        body = Existinguser()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example')]
        response = self.client.open(
            '/smt/validateUser',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
