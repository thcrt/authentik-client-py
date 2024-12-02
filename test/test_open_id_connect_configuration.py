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

from authentik_client.models.open_id_connect_configuration import OpenIDConnectConfiguration

class TestOpenIDConnectConfiguration(unittest.TestCase):
    """OpenIDConnectConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OpenIDConnectConfiguration:
        """Test OpenIDConnectConfiguration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OpenIDConnectConfiguration`
        """
        model = OpenIDConnectConfiguration()
        if include_optional:
            return OpenIDConnectConfiguration(
                issuer = '',
                authorization_endpoint = '',
                token_endpoint = '',
                userinfo_endpoint = '',
                end_session_endpoint = '',
                introspection_endpoint = '',
                jwks_uri = '',
                response_types_supported = [
                    ''
                    ],
                id_token_signing_alg_values_supported = [
                    ''
                    ],
                subject_types_supported = [
                    ''
                    ],
                token_endpoint_auth_methods_supported = [
                    ''
                    ]
            )
        else:
            return OpenIDConnectConfiguration(
                issuer = '',
                authorization_endpoint = '',
                token_endpoint = '',
                userinfo_endpoint = '',
                end_session_endpoint = '',
                introspection_endpoint = '',
                jwks_uri = '',
                response_types_supported = [
                    ''
                    ],
                id_token_signing_alg_values_supported = [
                    ''
                    ],
                subject_types_supported = [
                    ''
                    ],
                token_endpoint_auth_methods_supported = [
                    ''
                    ],
        )
        """

    def testOpenIDConnectConfiguration(self):
        """Test OpenIDConnectConfiguration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
