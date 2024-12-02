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

from authentik_client.models.endpoint_request import EndpointRequest

class TestEndpointRequest(unittest.TestCase):
    """EndpointRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EndpointRequest:
        """Test EndpointRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EndpointRequest`
        """
        model = EndpointRequest()
        if include_optional:
            return EndpointRequest(
                name = '0',
                provider = 56,
                protocol = 'rdp',
                host = '0',
                settings = None,
                property_mappings = [
                    ''
                    ],
                auth_mode = 'static',
                maximum_connections = -2147483648
            )
        else:
            return EndpointRequest(
                name = '0',
                provider = 56,
                protocol = 'rdp',
                host = '0',
                auth_mode = 'static',
        )
        """

    def testEndpointRequest(self):
        """Test EndpointRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
