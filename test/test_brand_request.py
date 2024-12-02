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

from authentik_client.models.brand_request import BrandRequest

class TestBrandRequest(unittest.TestCase):
    """BrandRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BrandRequest:
        """Test BrandRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BrandRequest`
        """
        model = BrandRequest()
        if include_optional:
            return BrandRequest(
                domain = '0',
                default = True,
                branding_title = '0',
                branding_logo = '0',
                branding_favicon = '0',
                flow_authentication = '',
                flow_invalidation = '',
                flow_recovery = '',
                flow_unenrollment = '',
                flow_user_settings = '',
                flow_device_code = '',
                default_application = '',
                web_certificate = '',
                attributes = None
            )
        else:
            return BrandRequest(
                domain = '0',
        )
        """

    def testBrandRequest(self):
        """Test BrandRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
