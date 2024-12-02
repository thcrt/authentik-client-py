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

from authentik_client.models.kerberos_source_property_mapping import KerberosSourcePropertyMapping

class TestKerberosSourcePropertyMapping(unittest.TestCase):
    """KerberosSourcePropertyMapping unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KerberosSourcePropertyMapping:
        """Test KerberosSourcePropertyMapping
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KerberosSourcePropertyMapping`
        """
        model = KerberosSourcePropertyMapping()
        if include_optional:
            return KerberosSourcePropertyMapping(
                pk = '',
                managed = '',
                name = '',
                expression = '',
                component = '',
                verbose_name = '',
                verbose_name_plural = '',
                meta_model_name = ''
            )
        else:
            return KerberosSourcePropertyMapping(
                pk = '',
                name = '',
                expression = '',
                component = '',
                verbose_name = '',
                verbose_name_plural = '',
                meta_model_name = '',
        )
        """

    def testKerberosSourcePropertyMapping(self):
        """Test KerberosSourcePropertyMapping"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
