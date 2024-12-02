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

from authentik_client.models.microsoft_entra_provider_user_request import MicrosoftEntraProviderUserRequest

class TestMicrosoftEntraProviderUserRequest(unittest.TestCase):
    """MicrosoftEntraProviderUserRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MicrosoftEntraProviderUserRequest:
        """Test MicrosoftEntraProviderUserRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MicrosoftEntraProviderUserRequest`
        """
        model = MicrosoftEntraProviderUserRequest()
        if include_optional:
            return MicrosoftEntraProviderUserRequest(
                microsoft_id = '0',
                user = 56,
                provider = 56
            )
        else:
            return MicrosoftEntraProviderUserRequest(
                microsoft_id = '0',
                user = 56,
                provider = 56,
        )
        """

    def testMicrosoftEntraProviderUserRequest(self):
        """Test MicrosoftEntraProviderUserRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
