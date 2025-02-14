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

from authentik_client.models.patched_kerberos_source_request import PatchedKerberosSourceRequest

class TestPatchedKerberosSourceRequest(unittest.TestCase):
    """PatchedKerberosSourceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedKerberosSourceRequest:
        """Test PatchedKerberosSourceRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedKerberosSourceRequest`
        """
        model = PatchedKerberosSourceRequest()
        if include_optional:
            return PatchedKerberosSourceRequest(
                name = '0',
                slug = 'z0',
                enabled = True,
                authentication_flow = '',
                enrollment_flow = '',
                user_property_mappings = [
                    ''
                    ],
                group_property_mappings = [
                    ''
                    ],
                policy_engine_mode = 'all',
                user_matching_mode = 'identifier',
                user_path_template = '0',
                group_matching_mode = 'identifier',
                realm = '0',
                krb5_conf = '',
                sync_users = True,
                sync_users_password = True,
                sync_principal = '',
                sync_password = '',
                sync_keytab = '',
                sync_ccache = '',
                spnego_server_name = '',
                spnego_keytab = '',
                spnego_ccache = '',
                password_login_update_internal_password = True
            )
        else:
            return PatchedKerberosSourceRequest(
        )
        """

    def testPatchedKerberosSourceRequest(self):
        """Test PatchedKerberosSourceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
