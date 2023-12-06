import connexion
import six

from swagger_server.models.err import Err  # noqa: E501
from swagger_server.models.submit_request import SubmitRequest  # noqa: E501
from swagger_server import util


def submit_request(body=None, kore_user_id=None, bot_id=None, account_id=None, authorization=None):  # noqa: E501
    """Submit Request

    Meta API request # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param kore_user_id: 
    :type kore_user_id: str
    :param bot_id: 
    :type bot_id: str
    :param account_id: 
    :type account_id: str
    :param authorization: 
    :type authorization: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = SubmitRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
