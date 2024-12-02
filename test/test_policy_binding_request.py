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

from authentik_client.models.policy_binding_request import PolicyBindingRequest

class TestPolicyBindingRequest(unittest.TestCase):
    """PolicyBindingRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PolicyBindingRequest:
        """Test PolicyBindingRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PolicyBindingRequest`
        """
        model = PolicyBindingRequest()
        if include_optional:
            return PolicyBindingRequest(
                policy = '',
                group = '',
                user = 56,
                target = '',
                negate = True,
                enabled = True,
                order = -2147483648,
                timeout = 0,
                failure_result = True
            )
        else:
            return PolicyBindingRequest(
                target = '',
                order = -2147483648,
        )
        """

    def testPolicyBindingRequest(self):
        """Test PolicyBindingRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
