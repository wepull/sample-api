import connexion
import six

from swagger_server.models.dispute_request import DisputeRequest  # noqa: E501
from swagger_server.models.err import Err  # noqa: E501
from swagger_server.models.get_transactions_req import GetTransactionsReq  # noqa: E501
from swagger_server.models.get_transactions_res import GetTransactionsRes  # noqa: E501
from swagger_server import util


def dispute_transaction(bot_id, account_id, authorization, body=None, kore_user_id=None):  # noqa: E501
    """disputeTransaction

    dispute a transaction # noqa: E501

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
        body = DisputeRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_transactions(body, bot_id, account_id, authorization, kore_user_id=None, x_auth_token=None, x_correlation_id=None):  # noqa: E501
    """GetTransactions

    Fetch transactions information # noqa: E501

    :param body: Transaction Request
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

    :rtype: GetTransactionsRes
    """
    if connexion.request.is_json:
        body = GetTransactionsReq.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
