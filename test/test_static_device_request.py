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

from authentik_client.models.static_device_request import StaticDeviceRequest

class TestStaticDeviceRequest(unittest.TestCase):
    """StaticDeviceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StaticDeviceRequest:
        """Test StaticDeviceRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StaticDeviceRequest`
        """
        model = StaticDeviceRequest()
        if include_optional:
            return StaticDeviceRequest(
                name = '0'
            )
        else:
            return StaticDeviceRequest(
                name = '0',
        )
        """

    def testStaticDeviceRequest(self):
        """Test StaticDeviceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
