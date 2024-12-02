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

from authentik_client.models.consent_challenge import ConsentChallenge

class TestConsentChallenge(unittest.TestCase):
    """ConsentChallenge unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConsentChallenge:
        """Test ConsentChallenge
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConsentChallenge`
        """
        model = ConsentChallenge()
        if include_optional:
            return ConsentChallenge(
                flow_info = authentik_client.models.contextual_flow_info.ContextualFlowInfo(
                    title = '', 
                    background = '', 
                    cancel_url = '', 
                    layout = 'stacked', ),
                component = 'ak-stage-consent',
                response_errors = {
                    'key' : [
                        authentik_client.models.error_detail.ErrorDetail(
                            string = '', 
                            code = '', )
                        ]
                    },
                pending_user = '',
                pending_user_avatar = '',
                header_text = '',
                permissions = [
                    authentik_client.models.consent_permission.ConsentPermission(
                        name = '', 
                        id = '', )
                    ],
                additional_permissions = [
                    authentik_client.models.consent_permission.ConsentPermission(
                        name = '', 
                        id = '', )
                    ],
                token = ''
            )
        else:
            return ConsentChallenge(
                pending_user = '',
                pending_user_avatar = '',
                permissions = [
                    authentik_client.models.consent_permission.ConsentPermission(
                        name = '', 
                        id = '', )
                    ],
                additional_permissions = [
                    authentik_client.models.consent_permission.ConsentPermission(
                        name = '', 
                        id = '', )
                    ],
                token = '',
        )
        """

    def testConsentChallenge(self):
        """Test ConsentChallenge"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
