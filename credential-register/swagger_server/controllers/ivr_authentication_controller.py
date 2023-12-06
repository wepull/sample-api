import connexion
import six

from swagger_server.models.err import Err  # noqa: E501
from swagger_server.models.existinguser import Existinguser  # noqa: E501
from swagger_server.models.newuser import Newuser  # noqa: E501
from swagger_server.models.newuserpinrules import Newuserpinrules  # noqa: E501
from swagger_server import util


def validate_pin(body, bot_id, account_id, authorization, kore_user_id=None):  # noqa: E501
    """to validate the pins entered by the new user

    to validate the pins entered by the new user # noqa: E501

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
        body = Newuser.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def validate_pin_rules(body, bot_id, account_id, authorization, kore_user_id=None):  # noqa: E501
    """to validate if pin entered by new user follows pin rules

    to validate if pin entered by new user follows pin rules # noqa: E501

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
        body = Newuserpinrules.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def validate_user(body, bot_id, account_id, authorization, kore_user_id=None):  # noqa: E501
    """to validate the exiting user

    to validate the in of existing user # noqa: E501

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
        body = Existinguser.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
