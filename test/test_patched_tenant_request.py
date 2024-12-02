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

from authentik_client.models.patched_tenant_request import PatchedTenantRequest

class TestPatchedTenantRequest(unittest.TestCase):
    """PatchedTenantRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedTenantRequest:
        """Test PatchedTenantRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedTenantRequest`
        """
        model = PatchedTenantRequest()
        if include_optional:
            return PatchedTenantRequest(
                schema_name = '0',
                name = '0',
                ready = True
            )
        else:
            return PatchedTenantRequest(
        )
        """

    def testPatchedTenantRequest(self):
        """Test PatchedTenantRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
