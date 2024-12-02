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

from authentik_client.models.ldap_outpost_config import LDAPOutpostConfig

class TestLDAPOutpostConfig(unittest.TestCase):
    """LDAPOutpostConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LDAPOutpostConfig:
        """Test LDAPOutpostConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LDAPOutpostConfig`
        """
        model = LDAPOutpostConfig()
        if include_optional:
            return LDAPOutpostConfig(
                pk = 56,
                name = '',
                base_dn = '',
                bind_flow_slug = '',
                unbind_flow_slug = '',
                application_slug = '',
                certificate = '',
                tls_server_name = '',
                uid_start_number = -2147483648,
                gid_start_number = -2147483648,
                search_mode = 'direct',
                bind_mode = 'direct',
                mfa_support = True
            )
        else:
            return LDAPOutpostConfig(
                pk = 56,
                name = '',
                bind_flow_slug = '',
                unbind_flow_slug = '',
                application_slug = '',
        )
        """

    def testLDAPOutpostConfig(self):
        """Test LDAPOutpostConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
