import connexion
import six

from swagger_server.models.err import Err  # noqa: E501
from swagger_server.models.request import Request  # noqa: E501
from swagger_server import util


def send_request(body, bot_id, account_id, authorization, kore_user_id=None):  # noqa: E501
    """to place the request

    to place the request # noqa: E501

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
        body = Request.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
