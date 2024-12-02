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

from authentik_client.models.geo_ip_policy_request import GeoIPPolicyRequest

class TestGeoIPPolicyRequest(unittest.TestCase):
    """GeoIPPolicyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GeoIPPolicyRequest:
        """Test GeoIPPolicyRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GeoIPPolicyRequest`
        """
        model = GeoIPPolicyRequest()
        if include_optional:
            return GeoIPPolicyRequest(
                name = '0',
                execution_logging = True,
                asns = [
                    -2147483648
                    ],
                countries = [
                    'AF'
                    ]
            )
        else:
            return GeoIPPolicyRequest(
                name = '0',
                countries = [
                    'AF'
                    ],
        )
        """

    def testGeoIPPolicyRequest(self):
        """Test GeoIPPolicyRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
