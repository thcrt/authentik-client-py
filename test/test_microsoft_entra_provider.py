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

from authentik_client.models.microsoft_entra_provider import MicrosoftEntraProvider

class TestMicrosoftEntraProvider(unittest.TestCase):
    """MicrosoftEntraProvider unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MicrosoftEntraProvider:
        """Test MicrosoftEntraProvider
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MicrosoftEntraProvider`
        """
        model = MicrosoftEntraProvider()
        if include_optional:
            return MicrosoftEntraProvider(
                pk = 56,
                name = '',
                property_mappings = [
                    ''
                    ],
                property_mappings_group = [
                    ''
                    ],
                component = '',
                assigned_backchannel_application_slug = '',
                assigned_backchannel_application_name = '',
                verbose_name = '',
                verbose_name_plural = '',
                meta_model_name = '',
                client_id = '',
                client_secret = '',
                tenant_id = '',
                exclude_users_service_account = True,
                filter_group = '',
                user_delete_action = 'do_nothing',
                group_delete_action = 'do_nothing'
            )
        else:
            return MicrosoftEntraProvider(
                pk = 56,
                name = '',
                component = '',
                assigned_backchannel_application_slug = '',
                assigned_backchannel_application_name = '',
                verbose_name = '',
                verbose_name_plural = '',
                meta_model_name = '',
                client_id = '',
                client_secret = '',
                tenant_id = '',
        )
        """

    def testMicrosoftEntraProvider(self):
        """Test MicrosoftEntraProvider"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
