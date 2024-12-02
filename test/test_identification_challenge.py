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

from authentik_client.models.identification_challenge import IdentificationChallenge

class TestIdentificationChallenge(unittest.TestCase):
    """IdentificationChallenge unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdentificationChallenge:
        """Test IdentificationChallenge
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdentificationChallenge`
        """
        model = IdentificationChallenge()
        if include_optional:
            return IdentificationChallenge(
                flow_info = authentik_client.models.contextual_flow_info.ContextualFlowInfo(
                    title = '', 
                    background = '', 
                    cancel_url = '', 
                    layout = 'stacked', ),
                component = 'ak-stage-identification',
                response_errors = {
                    'key' : [
                        authentik_client.models.error_detail.ErrorDetail(
                            string = '', 
                            code = '', )
                        ]
                    },
                user_fields = [
                    ''
                    ],
                password_fields = True,
                allow_show_password = True,
                application_pre = '',
                flow_designation = 'authentication',
                captcha_stage = authentik_client.models.captcha_challenge.CaptchaChallenge(
                    flow_info = authentik_client.models.contextual_flow_info.ContextualFlowInfo(
                        title = '', 
                        background = '', 
                        cancel_url = '', 
                        layout = 'stacked', ), 
                    component = 'ak-stage-captcha', 
                    response_errors = {
                        'key' : [
                            authentik_client.models.error_detail.ErrorDetail(
                                string = '', 
                                code = '', )
                            ]
                        }, 
                    pending_user = '', 
                    pending_user_avatar = '', 
                    site_key = '', 
                    js_url = '', 
                    interactive = True, ),
                enroll_url = '',
                recovery_url = '',
                passwordless_url = '',
                primary_action = '',
                sources = [
                    authentik_client.models.login_source.LoginSource(
                        name = '', 
                        icon_url = '', 
                        challenge = null, )
                    ],
                show_source_labels = True
            )
        else:
            return IdentificationChallenge(
                user_fields = [
                    ''
                    ],
                password_fields = True,
                flow_designation = 'authentication',
                primary_action = '',
                show_source_labels = True,
        )
        """

    def testIdentificationChallenge(self):
        """Test IdentificationChallenge"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
