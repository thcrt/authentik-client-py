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

from authentik_client.models.authenticator_validate_stage import AuthenticatorValidateStage

class TestAuthenticatorValidateStage(unittest.TestCase):
    """AuthenticatorValidateStage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthenticatorValidateStage:
        """Test AuthenticatorValidateStage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthenticatorValidateStage`
        """
        model = AuthenticatorValidateStage()
        if include_optional:
            return AuthenticatorValidateStage(
                pk = '',
                name = '',
                component = '',
                verbose_name = '',
                verbose_name_plural = '',
                meta_model_name = '',
                flow_set = [
                    authentik_client.models.flow_set.FlowSet(
                        pk = '', 
                        policybindingmodel_ptr_id = '', 
                        name = '', 
                        slug = 'z', 
                        title = '', 
                        designation = null, 
                        background = '', 
                        policy_engine_mode = 'all', 
                        compatibility_mode = True, 
                        export_url = '', 
                        layout = 'stacked', 
                        denied_action = null, )
                    ],
                not_configured_action = 'skip',
                device_classes = [
                    'static'
                    ],
                configuration_stages = [
                    ''
                    ],
                last_auth_threshold = '',
                webauthn_user_verification = 'required',
                webauthn_allowed_device_types = [
                    ''
                    ],
                webauthn_allowed_device_types_obj = [
                    authentik_client.models.web_authn_device_type.WebAuthnDeviceType(
                        aaguid = '', 
                        description = '', )
                    ]
            )
        else:
            return AuthenticatorValidateStage(
                pk = '',
                name = '',
                component = '',
                verbose_name = '',
                verbose_name_plural = '',
                meta_model_name = '',
                webauthn_allowed_device_types_obj = [
                    authentik_client.models.web_authn_device_type.WebAuthnDeviceType(
                        aaguid = '', 
                        description = '', )
                    ],
        )
        """

    def testAuthenticatorValidateStage(self):
        """Test AuthenticatorValidateStage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
