import connexion
import six

from swagger_server.models.err import Err  # noqa: E501
from swagger_server.models.secure_message_request import SecureMessageRequest  # noqa: E501
from swagger_server import util


def sendsecuremessage(bot_id, account_id, authorization, body=None, kore_user_id=None):  # noqa: E501
    """sendsecuremessage

    send secure message # noqa: E501

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
        body = SecureMessageRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
