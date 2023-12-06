import connexion
import six

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
from swagger_server import util


def deposit(bot_id, account_id, authorization, body=None, kore_user_id=None):  # noqa: E501
    """Deposit

    Deposit amount to customer&#x27;s account # noqa: E501

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
        body = DepositRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_account_details(body, bot_id, account_id, authorization, kore_user_id=None, x_auth_token=None, x_correlation_id=None):  # noqa: E501
    """to get the details of the mentioned customer account

    fetch customer account details # noqa: E501

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
    :param x_auth_token: 
    :type x_auth_token: str
    :param x_correlation_id: 
    :type x_correlation_id: float

    :rtype: GetAccountResponse
    """
    if connexion.request.is_json:
        body = AccountDetailsRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_account_info(body, bot_id, account_id, authorization, kore_user_id=None, x_auth_token=None, x_correlation_id=None):  # noqa: E501
    """GetAccountInfo

    fetch customer account details # noqa: E501

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
    :param x_auth_token: 
    :type x_auth_token: str
    :param x_correlation_id: 
    :type x_correlation_id: float

    :rtype: GetAccountData
    """
    if connexion.request.is_json:
        body = AccountRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_account_specific_limits_info(body, bot_id, account_id, authorization, kore_user_id=None, x_auth_token=None, x_correlation_id=None):  # noqa: E501
    """to get the limits of customer accounts

    fetch customer account limits # noqa: E501

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
    :param x_auth_token: 
    :type x_auth_token: str
    :param x_correlation_id: 
    :type x_correlation_id: float

    :rtype: ViewlimitsResponse
    """
    if connexion.request.is_json:
        body = ViewLimitRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_accounts_limit(body, bot_id, account_id, authorization, kore_user_id=None, x_auth_token=None, x_correlation_id=None):  # noqa: E501
    """to get the limits of customer accounts

    fetch customer account limits # noqa: E501

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
    :param x_auth_token: 
    :type x_auth_token: str
    :param x_correlation_id: 
    :type x_correlation_id: float

    :rtype: LimitsResponse
    """
    if connexion.request.is_json:
        body = LimitRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_request_status(body, bot_id, account_id, authorization, kore_user_id=None):  # noqa: E501
    """to fetch the account closure status

    to fetch the account closure status # noqa: E501

    :param body: 
    :type body: list | bytes
    :param bot_id: 
    :type bot_id: str
    :param account_id: 
    :type account_id: str
    :param authorization: 
    :type authorization: str
    :param kore_user_id: 
    :type kore_user_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = [RequestStatusResponseInner.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def request_cheque_book(body, bot_id, account_id, authorization, kore_user_id=None):  # noqa: E501
    """to update the cheque book details of customer accounts

    Update customer cheque book details # noqa: E501

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

    :rtype: None
    """
    if connexion.request.is_json:
        body = ChequeBookRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_account_info(body, bot_id, account_id, authorization, kore_user_id=None, x_auth_token=None, x_correlation_id=None):  # noqa: E501
    """UpdateAccountInfo

    Update customer account details # noqa: E501

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
    :param x_auth_token: 
    :type x_auth_token: str
    :param x_correlation_id: 
    :type x_correlation_id: float

    :rtype: None
    """
    if connexion.request.is_json:
        body = UpdateaccountRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
