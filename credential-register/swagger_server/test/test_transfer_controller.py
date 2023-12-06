# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.cc_list_response import CCListResponse  # noqa: E501
from swagger_server.models.cc_request import CcRequest  # noqa: E501
from swagger_server.models.cc_schedule_request import CcScheduleRequest  # noqa: E501
from swagger_server.models.delete_recurring_transfer_request import DeleteRecurringTransferRequest  # noqa: E501
from swagger_server.models.delete_schedule_transfer_request import DeleteScheduleTransferRequest  # noqa: E501
from swagger_server.models.err import Err  # noqa: E501
from swagger_server.models.transfer_recurring_add_request import TransferRecurringAddRequest  # noqa: E501
from swagger_server.models.transfer_recurring_list_request import TransferRecurringListRequest  # noqa: E501
from swagger_server.models.transfer_recurring_list_response import TransferRecurringListResponse  # noqa: E501
from swagger_server.models.transfer_recurring_update_request import TransferRecurringUpdateRequest  # noqa: E501
from swagger_server.models.transfer_request import TransferRequest  # noqa: E501
from swagger_server.models.transfer_schedule_list_request import TransferScheduleListRequest  # noqa: E501
from swagger_server.models.transfer_schedule_list_response import TransferScheduleListResponse  # noqa: E501
from swagger_server.models.transfer_schedule_update_request import TransferScheduleUpdateRequest  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTransferController(BaseTestCase):
    """TransferController integration test stubs"""

    def test_add_recurring_transfers(self):
        """Test case for add_recurring_transfers

        AddRecurringTransfers
        """
        body = TransferRecurringAddRequest()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('user_code', 'user_code_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example')]
        response = self.client.open(
            '/smt/AddRecurringTransfers',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cc_pay(self):
        """Test case for cc_pay

        ccPay
        """
        body = CcRequest()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example')]
        response = self.client.open(
            '/smt/ccPay',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_recurring_transfers(self):
        """Test case for delete_recurring_transfers

        DeleteRecurringTransfers
        """
        body = DeleteRecurringTransferRequest()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('user_code', 'user_code_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example')]
        response = self.client.open(
            '/smt/DeleteRecurringTransfers',
            method='DELETE',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_schedule_transfers(self):
        """Test case for delete_schedule_transfers

        DeleteScheduleTransfers
        """
        body = DeleteScheduleTransferRequest()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('user_code', 'user_code_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example')]
        response = self.client.open(
            '/smt/DeleteScheduleTransfers',
            method='DELETE',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_cc_schedule(self):
        """Test case for get_cc_schedule

        GetCCSchedule
        """
        body = CcScheduleRequest()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example')]
        response = self.client.open(
            '/smt/GetCCSchedule',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_recurring_transfers(self):
        """Test case for get_recurring_transfers

        GetRecurringTransfers
        """
        body = TransferRecurringListRequest()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('user_code', 'user_code_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example')]
        response = self.client.open(
            '/smt/GetRecurringTransfers',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_schedule_transfers(self):
        """Test case for get_schedule_transfers

        GetScheduleTransfers
        """
        body = TransferScheduleListRequest()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('user_code', 'user_code_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example')]
        response = self.client.open(
            '/smt/GetScheduleTransfers',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_transfer_funds(self):
        """Test case for transfer_funds

        TransferFunds
        """
        body = TransferRequest()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('user_code', 'user_code_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example')]
        response = self.client.open(
            '/smt/TransferFunds',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_recurring_transfers(self):
        """Test case for update_recurring_transfers

        UpdateRecurringTransfers
        """
        body = TransferRecurringUpdateRequest()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('user_code', 'user_code_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example')]
        response = self.client.open(
            '/smt/UpdateRecurringTransfers',
            method='PUT',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_schedule_transfers(self):
        """Test case for update_schedule_transfers

        UpdateScheduleTransfers
        """
        body = TransferScheduleUpdateRequest()
        headers = [('kore_user_id', 'kore_user_id_example'),
                   ('bot_id', 'bot_id_example'),
                   ('user_code', 'user_code_example'),
                   ('account_id', 'account_id_example'),
                   ('authorization', 'authorization_example')]
        response = self.client.open(
            '/smt/UpdateScheduleTransfers',
            method='PUT',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
