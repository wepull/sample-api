import connexion
import six

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
from swagger_server import util


def add_recurring_transfers(bot_id, account_id, authorization, body=None, kore_user_id=None, user_code=None):  # noqa: E501
    """AddRecurringTransfers

    Adds the recurring transfers # noqa: E501

    :param bot_id: 
    :type bot_id: str
    :param account_id: 
    :type account_id: str
    :param authorization: 
    :type authorization: str
    :param body: 
    :type body: dict | bytes
    :param kore_user_id: 
    :type kore_user_id: str
    :param user_code: 
    :type user_code: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = TransferRecurringAddRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def cc_pay(bot_id, account_id, authorization, body=None, kore_user_id=None):  # noqa: E501
    """ccPay

    to pay cc bill # noqa: E501

    :param bot_id: 
    :type bot_id: str
    :param account_id: 
    :type account_id: str
    :param authorization: 
    :type authorization: str
    :param body: 
    :type body: dict | bytes
    :param kore_user_id: 
    :type kore_user_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = CcRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_recurring_transfers(bot_id, account_id, authorization, body=None, kore_user_id=None, user_code=None):  # noqa: E501
    """DeleteRecurringTransfers

    Delete the recurring transfers # noqa: E501

    :param bot_id: 
    :type bot_id: str
    :param account_id: 
    :type account_id: str
    :param authorization: 
    :type authorization: str
    :param body: 
    :type body: dict | bytes
    :param kore_user_id: 
    :type kore_user_id: str
    :param user_code: 
    :type user_code: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = DeleteRecurringTransferRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_schedule_transfers(bot_id, account_id, authorization, body=None, kore_user_id=None, user_code=None):  # noqa: E501
    """DeleteScheduleTransfers

    Delete the scheduled transfer # noqa: E501

    :param bot_id: 
    :type bot_id: str
    :param account_id: 
    :type account_id: str
    :param authorization: 
    :type authorization: str
    :param body: 
    :type body: dict | bytes
    :param kore_user_id: 
    :type kore_user_id: str
    :param user_code: 
    :type user_code: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = DeleteScheduleTransferRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_cc_schedule(bot_id, account_id, authorization, body=None, kore_user_id=None):  # noqa: E501
    """GetCCSchedule

    Fetch cc payment list # noqa: E501

    :param bot_id: 
    :type bot_id: str
    :param account_id: 
    :type account_id: str
    :param authorization: 
    :type authorization: str
    :param body: 
    :type body: dict | bytes
    :param kore_user_id: 
    :type kore_user_id: str

    :rtype: CCListResponse
    """
    if connexion.request.is_json:
        body = CcScheduleRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_recurring_transfers(bot_id, account_id, authorization, body=None, kore_user_id=None, user_code=None):  # noqa: E501
    """GetRecurringTransfers

    Fetches all the recurring transfers # noqa: E501

    :param bot_id: 
    :type bot_id: str
    :param account_id: 
    :type account_id: str
    :param authorization: 
    :type authorization: str
    :param body: 
    :type body: dict | bytes
    :param kore_user_id: 
    :type kore_user_id: str
    :param user_code: 
    :type user_code: str

    :rtype: TransferRecurringListResponse
    """
    if connexion.request.is_json:
        body = TransferRecurringListRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_schedule_transfers(bot_id, account_id, authorization, body=None, kore_user_id=None, user_code=None):  # noqa: E501
    """GetScheduleTransfers

    Fetches the scheduled transfers # noqa: E501

    :param bot_id: 
    :type bot_id: str
    :param account_id: 
    :type account_id: str
    :param authorization: 
    :type authorization: str
    :param body: 
    :type body: dict | bytes
    :param kore_user_id: 
    :type kore_user_id: str
    :param user_code: 
    :type user_code: str

    :rtype: TransferScheduleListResponse
    """
    if connexion.request.is_json:
        body = TransferScheduleListRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def transfer_funds(body, bot_id, account_id, authorization, kore_user_id=None, user_code=None):  # noqa: E501
    """TransferFunds

    Transfers funds between accounts # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param bot_id: 
    :type bot_id: str
    :param account_id: 
    :type account_id: str
    :param authorization: 
    :type authorization: str
    :param kore_user_id: 
    :type kore_user_id: str
    :param user_code: 
    :type user_code: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = TransferRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_recurring_transfers(bot_id, account_id, authorization, body=None, kore_user_id=None, user_code=None):  # noqa: E501
    """UpdateRecurringTransfers

    Update the recurring transfers # noqa: E501

    :param bot_id: 
    :type bot_id: str
    :param account_id: 
    :type account_id: str
    :param authorization: 
    :type authorization: str
    :param body: 
    :type body: dict | bytes
    :param kore_user_id: 
    :type kore_user_id: str
    :param user_code: 
    :type user_code: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = TransferRecurringUpdateRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_schedule_transfers(bot_id, account_id, authorization, body=None, kore_user_id=None, user_code=None):  # noqa: E501
    """UpdateScheduleTransfers

    Update the scheduled transfers # noqa: E501

    :param bot_id: 
    :type bot_id: str
    :param account_id: 
    :type account_id: str
    :param authorization: 
    :type authorization: str
    :param body: 
    :type body: dict | bytes
    :param kore_user_id: 
    :type kore_user_id: str
    :param user_code: 
    :type user_code: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = TransferScheduleUpdateRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
