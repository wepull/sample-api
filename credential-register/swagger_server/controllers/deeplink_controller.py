import connexion
import six

from swagger_server.models.deeplink import Deeplink  # noqa: E501
from swagger_server.models.deeplinkresponse import Deeplinkresponse  # noqa: E501
from swagger_server.models.err import Err  # noqa: E501
from swagger_server import util


def get_deeplink(body=None, kore_user_id=None, bot_id=None, account_id=None, tenant_id=None, authorization=None, environment=None, channel=None):  # noqa: E501
    """to fetch the deeplink

    to fetch the deeplink # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param kore_user_id: 
    :type kore_user_id: str
    :param bot_id: 
    :type bot_id: str
    :param account_id: 
    :type account_id: str
    :param tenant_id: 
    :type tenant_id: str
    :param authorization: 
    :type authorization: str
    :param environment: 
    :type environment: str
    :param channel: 
    :type channel: str

    :rtype: Deeplinkresponse
    """
    if connexion.request.is_json:
        body = Deeplink.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
