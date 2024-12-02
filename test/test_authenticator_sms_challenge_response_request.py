# coding: utf-8

"""
    authentik

    Making authentication simple.

    The version of the OpenAPI document: 2024.10.4
    Contact: hello@goauthentik.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from authentik_client.models.authenticator_sms_challenge_response_request import AuthenticatorSMSChallengeResponseRequest

class TestAuthenticatorSMSChallengeResponseRequest(unittest.TestCase):
    """AuthenticatorSMSChallengeResponseRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthenticatorSMSChallengeResponseRequest:
        """Test AuthenticatorSMSChallengeResponseRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthenticatorSMSChallengeResponseRequest`
        """
        model = AuthenticatorSMSChallengeResponseRequest()
        if include_optional:
            return AuthenticatorSMSChallengeResponseRequest(
                component = 'ak-stage-authenticator-sms',
                code = 56,
                phone_number = '0'
            )
        else:
            return AuthenticatorSMSChallengeResponseRequest(
        )
        """

    def testAuthenticatorSMSChallengeResponseRequest(self):
        """Test AuthenticatorSMSChallengeResponseRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
