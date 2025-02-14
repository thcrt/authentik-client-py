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

from authentik_client.models.authenticator_static_challenge import AuthenticatorStaticChallenge

class TestAuthenticatorStaticChallenge(unittest.TestCase):
    """AuthenticatorStaticChallenge unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthenticatorStaticChallenge:
        """Test AuthenticatorStaticChallenge
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthenticatorStaticChallenge`
        """
        model = AuthenticatorStaticChallenge()
        if include_optional:
            return AuthenticatorStaticChallenge(
                flow_info = authentik_client.models.contextual_flow_info.ContextualFlowInfo(
                    title = '', 
                    background = '', 
                    cancel_url = '', 
                    layout = 'stacked', ),
                component = 'ak-stage-authenticator-static',
                response_errors = {
                    'key' : [
                        authentik_client.models.error_detail.ErrorDetail(
                            string = '', 
                            code = '', )
                        ]
                    },
                pending_user = '',
                pending_user_avatar = '',
                codes = [
                    ''
                    ]
            )
        else:
            return AuthenticatorStaticChallenge(
                pending_user = '',
                pending_user_avatar = '',
                codes = [
                    ''
                    ],
        )
        """

    def testAuthenticatorStaticChallenge(self):
        """Test AuthenticatorStaticChallenge"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
