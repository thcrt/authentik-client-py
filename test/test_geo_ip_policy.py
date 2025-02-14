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

from authentik_client.models.geo_ip_policy import GeoIPPolicy

class TestGeoIPPolicy(unittest.TestCase):
    """GeoIPPolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GeoIPPolicy:
        """Test GeoIPPolicy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GeoIPPolicy`
        """
        model = GeoIPPolicy()
        if include_optional:
            return GeoIPPolicy(
                pk = '',
                name = '',
                execution_logging = True,
                component = '',
                verbose_name = '',
                verbose_name_plural = '',
                meta_model_name = '',
                bound_to = 56,
                asns = [
                    -2147483648
                    ],
                countries = [
                    'AF'
                    ],
                countries_obj = [
                    authentik_client.models.detailed_country_field.DetailedCountryField(
                        code = 'AF', 
                        name = '', )
                    ]
            )
        else:
            return GeoIPPolicy(
                pk = '',
                name = '',
                component = '',
                verbose_name = '',
                verbose_name_plural = '',
                meta_model_name = '',
                bound_to = 56,
                countries = [
                    'AF'
                    ],
                countries_obj = [
                    authentik_client.models.detailed_country_field.DetailedCountryField(
                        code = 'AF', 
                        name = '', )
                    ],
        )
        """

    def testGeoIPPolicy(self):
        """Test GeoIPPolicy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
