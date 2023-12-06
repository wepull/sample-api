# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.dispute_request import DisputeRequest  # noqa: E501
from swagger_server.models.err import Err  # noqa: E501
from swagger_server.models.get_transactions_req import GetTransactionsReq  # noqa: E501
from swagger_server.models.get_transactions_res import GetTransactionsRes  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTransactionsController(BaseTestCase):
    """TransactionsController integration test stubs"""

    def test_dispute_transaction(self):
        """Test case for dispute_transaction

        disputeTransaction
        """
        body = DisputeRequest()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example')]
        response = self.client.open(
            '/smt/disputeTransaction',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_transactions(self):
        """Test case for get_transactions

        GetTransactions
        """
        body = GetTransactionsReq()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example'),
                   ('x_auth_token', 'x_auth_token_example'),
                   ('x_correlation_id', 1.2)]
        response = self.client.open(
            '/smt/GetTransactions',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
