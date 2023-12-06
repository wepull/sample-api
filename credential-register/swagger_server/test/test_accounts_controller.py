# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.account_details_request import AccountDetailsRequest  # noqa: E501
from swagger_server.models.account_request import AccountRequest  # noqa: E501
from swagger_server.models.cheque_book_request import ChequeBookRequest  # noqa: E501
from swagger_server.models.deposit_request import DepositRequest  # noqa: E501
from swagger_server.models.err import Err  # noqa: E501
from swagger_server.models.get_account_data import GetAccountData  # noqa: E501
from swagger_server.models.get_account_response import GetAccountResponse  # noqa: E501
from swagger_server.models.limit_request import LimitRequest  # noqa: E501
from swagger_server.models.limits_response import LimitsResponse  # noqa: E501
from swagger_server.models.request_status_response_inner import RequestStatusResponseInner  # noqa: E501
from swagger_server.models.updateaccount_request import UpdateaccountRequest  # noqa: E501
from swagger_server.models.view_limit_request import ViewLimitRequest  # noqa: E501
from swagger_server.models.viewlimits_response import ViewlimitsResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAccountsController(BaseTestCase):
    """AccountsController integration test stubs"""

    def test_deposit(self):
        """Test case for deposit

        Deposit
        """
        body = DepositRequest()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example')]
        response = self.client.open(
            '/smt/deposit',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_account_details(self):
        """Test case for get_account_details

        to get the details of the mentioned customer account
        """
        body = AccountDetailsRequest()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example'),
                   ('x_auth_token', 'x_auth_token_example'),
                   ('x_correlation_id', 1.2)]
        response = self.client.open(
            '/smt/GetAccountDetails',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_account_info(self):
        """Test case for get_account_info

        GetAccountInfo
        """
        body = AccountRequest()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example'),
                   ('x_auth_token', 'x_auth_token_example'),
                   ('x_correlation_id', 1.2)]
        response = self.client.open(
            '/smt/GetAccountInfo',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_account_specific_limits_info(self):
        """Test case for get_account_specific_limits_info

        to get the limits of customer accounts
        """
        body = ViewLimitRequest()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example'),
                   ('x_auth_token', 'x_auth_token_example'),
                   ('x_correlation_id', 1.2)]
        response = self.client.open(
            '/smt/GetAccountSpecificLimitsInfo',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_accounts_limit(self):
        """Test case for get_accounts_limit

        to get the limits of customer accounts
        """
        body = LimitRequest()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example'),
                   ('x_auth_token', 'x_auth_token_example'),
                   ('x_correlation_id', 1.2)]
        response = self.client.open(
            '/smt/GetAccountsLimit',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_request_status(self):
        """Test case for get_request_status

        to fetch the account closure status
        """
        body = [RequestStatusResponseInner()]
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example')]
        response = self.client.open(
            '/smt/getRequestStatus',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_request_cheque_book(self):
        """Test case for request_cheque_book

        to update the cheque book details of customer accounts
        """
        body = ChequeBookRequest()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example')]
        response = self.client.open(
            '/smt/RequestChequeBook',
            method='PUT',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_account_info(self):
        """Test case for update_account_info

        UpdateAccountInfo
        """
        body = UpdateaccountRequest()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example'),
                   ('x_auth_token', 'x_auth_token_example'),
                   ('x_correlation_id', 1.2)]
        response = self.client.open(
            '/smt/UpdateAccountInfo',
            method='PUT',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
