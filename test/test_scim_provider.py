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

from authentik_client.models.scim_provider import SCIMProvider

class TestSCIMProvider(unittest.TestCase):
    """SCIMProvider unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SCIMProvider:
        """Test SCIMProvider
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SCIMProvider`
        """
        model = SCIMProvider()
        if include_optional:
            return SCIMProvider(
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
                url = '',
                verify_certificates = True,
                token = '',
                exclude_users_service_account = True,
                filter_group = ''
            )
        else:
            return SCIMProvider(
                pk = 56,
                name = '',
                component = '',
                assigned_backchannel_application_slug = '',
                assigned_backchannel_application_name = '',
                verbose_name = '',
                verbose_name_plural = '',
                meta_model_name = '',
                url = '',
                token = '',
        )
        """

    def testSCIMProvider(self):
        """Test SCIMProvider"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
