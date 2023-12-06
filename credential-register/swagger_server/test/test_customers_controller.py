# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.customer_request import CustomerRequest  # noqa: E501
from swagger_server.models.debitcard_infobody import DebitcardInfobody  # noqa: E501
from swagger_server.models.err import Err  # noqa: E501
from swagger_server.models.get_customer_data import GetCustomerData  # noqa: E501
from swagger_server.models.locate_profile_request import LocateProfileRequest  # noqa: E501
from swagger_server.models.locate_profile_response import LocateProfileResponse  # noqa: E501
from swagger_server.models.otp_request import OTPRequest  # noqa: E501
from swagger_server.models.personal_infobody import PersonalInfobody  # noqa: E501
from swagger_server.models.profile_e_statement_request import ProfileEStatementRequest  # noqa: E501
from swagger_server.models.resetpassword_body import ResetpasswordBody  # noqa: E501
from swagger_server.models.update_customer_request import UpdateCustomerRequest  # noqa: E501
from swagger_server.models.verify_ot_pbody import VerifyOTPbody  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCustomersController(BaseTestCase):
    """CustomersController integration test stubs"""

    def test_debitcard_info_validation(self):
        """Test case for debitcard_info_validation

        debitcardInfoValidation
        """
        body = DebitcardInfobody()
        response = self.client.open(
            '/smt/debitcardInfoValidation',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_enable_e_statement(self):
        """Test case for enable_e_statement

        to enable or disable e or paper statements at profile level
        """
        body = ProfileEStatementRequest()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example')]
        response = self.client.open(
            '/smt/enableEStatement',
            method='PUT',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_customer_info(self):
        """Test case for get_customer_info

        GetCustomerInfo
        """
        body = CustomerRequest()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example'),
                   ('x_auth_token', 'x_auth_token_example'),
                   ('x_correlation_id', 1.2)]
        response = self.client.open(
            '/smt/GetCustomerInfo',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_locate_profile(self):
        """Test case for locate_profile

        locateProfile
        """
        body = LocateProfileRequest()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example')]
        response = self.client.open(
            '/smt/locateProfile',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_personal_info_validation(self):
        """Test case for personal_info_validation

        personalInfoValidation
        """
        body = PersonalInfobody()
        response = self.client.open(
            '/smt/personalInfoValidation',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_reset_password(self):
        """Test case for reset_password

        resetPassword
        """
        body = ResetpasswordBody()
        response = self.client.open(
            '/smt/resetPassword',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_send_otp(self):
        """Test case for send_otp

        sendOTP
        """
        body = OTPRequest()
        response = self.client.open(
            '/smt/sendOTP',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_customer_info(self):
        """Test case for update_customer_info

        UpdateCustomerInfo
        """
        body = UpdateCustomerRequest()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example'),
                   ('x_auth_token', 'x_auth_token_example'),
                   ('x_correlation_id', 1.2)]
        response = self.client.open(
            '/smt/UpdateCustomerInfo',
            method='PUT',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_verify_otp(self):
        """Test case for verify_otp

        verifyOTP
        """
        body = VerifyOTPbody()
        response = self.client.open(
            '/smt/verifyOTP',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
