import connexion
import six

from swagger_server.models.err import Err  # noqa: E501
from swagger_server.models.get_auth_token_response import GetAuthTokenResponse  # noqa: E501
from swagger_server import util


def auth_token(authorization, kore_user_id=None, bot_id=None, account_id=None):  # noqa: E501
    """AuthToken

    Get authentication token # noqa: E501

    :param authorization: 
    :type authorization: str
    :param kore_user_id: 
    :type kore_user_id: str
    :param bot_id: 
    :type bot_id: str
    :param account_id: 
    :type account_id: str

    :rtype: GetAuthTokenResponse
    """
    return 'do some magic!'
