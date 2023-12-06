import connexion
import six

from swagger_server.models.customer_request import CustomerRequest  # noqa: E501
from swagger_server.models.debitcard_infobody import DebitcardInfobody  # noqa: E501
from swagger_server.models.err import Err  # noqa: E501
from swagger_server.models.get_customer_data import GetCustomerData  # noqa: E501
from swagger_server.models.locate_profile_request import LocateProfileRequest  # noqa: E501
from swagger_server.models.locate_profile_response import LocateProfileResponse  # noqa: E501
from swagger_server.models.otp_request import OTPRequest  # noqa: E501
from swagger_server.models.personal_infobody import PersonalInfobody  # noqa: E501
from swagger_server.models.profile_e_statement_request import ProfileEStatementRequest  # noqa: E501
from swagger_server.models.resetpassword_body import ResetpasswordBody  # noqa: E501
from swagger_server.models.update_customer_request import UpdateCustomerRequest  # noqa: E501
from swagger_server.models.verify_ot_pbody import VerifyOTPbody  # noqa: E501
from swagger_server import util


def debitcard_info_validation(body=None):  # noqa: E501
    """debitcardInfoValidation

    for validating card info # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = DebitcardInfobody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def enable_e_statement(body, bot_id, account_id, authorization, kore_user_id=None):  # noqa: E501
    """to enable or disable e or paper statements at profile level

    to enable or disable e or paper statements at profile level # noqa: E501

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
        body = ProfileEStatementRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_customer_info(body, bot_id, account_id, authorization, kore_user_id=None, x_auth_token=None, x_correlation_id=None):  # noqa: E501
    """GetCustomerInfo

    fetch customer information # noqa: E501

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

    :rtype: GetCustomerData
    """
    if connexion.request.is_json:
        body = CustomerRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def locate_profile(body, bot_id, account_id, authorization, kore_user_id=None):  # noqa: E501
    """locateProfile

    get profile details # noqa: E501

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

    :rtype: LocateProfileResponse
    """
    if connexion.request.is_json:
        body = LocateProfileRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def personal_info_validation(body=None):  # noqa: E501
    """personalInfoValidation

    for validating personal info # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PersonalInfobody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def reset_password(body=None):  # noqa: E501
    """resetPassword

    It allows to reset the password # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ResetpasswordBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def send_otp(body=None):  # noqa: E501
    """sendOTP

    sends OTP for reset password # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = OTPRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_customer_info(body, bot_id, account_id, authorization, kore_user_id=None, x_auth_token=None, x_correlation_id=None):  # noqa: E501
    """UpdateCustomerInfo

    Update customer information # noqa: E501

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
        body = UpdateCustomerRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def verify_otp(body=None):  # noqa: E501
    """verifyOTP

     to verify OTP for reset password # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = VerifyOTPbody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
