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

from authentik_client.models.reputation_policy_request import ReputationPolicyRequest

class TestReputationPolicyRequest(unittest.TestCase):
    """ReputationPolicyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReputationPolicyRequest:
        """Test ReputationPolicyRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReputationPolicyRequest`
        """
        model = ReputationPolicyRequest()
        if include_optional:
            return ReputationPolicyRequest(
                name = '0',
                execution_logging = True,
                check_ip = True,
                check_username = True,
                threshold = -2147483648
            )
        else:
            return ReputationPolicyRequest(
                name = '0',
        )
        """

    def testReputationPolicyRequest(self):
        """Test ReputationPolicyRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
