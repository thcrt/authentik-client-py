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

from authentik_client.models.license_request import LicenseRequest

class TestLicenseRequest(unittest.TestCase):
    """LicenseRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LicenseRequest:
        """Test LicenseRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LicenseRequest`
        """
        model = LicenseRequest()
        if include_optional:
            return LicenseRequest(
                key = '0'
            )
        else:
            return LicenseRequest(
                key = '0',
        )
        """

    def testLicenseRequest(self):
        """Test LicenseRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
