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

from authentik_client.models.flow_stage_binding_request import FlowStageBindingRequest

class TestFlowStageBindingRequest(unittest.TestCase):
    """FlowStageBindingRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FlowStageBindingRequest:
        """Test FlowStageBindingRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FlowStageBindingRequest`
        """
        model = FlowStageBindingRequest()
        if include_optional:
            return FlowStageBindingRequest(
                target = '',
                stage = '',
                evaluate_on_plan = True,
                re_evaluate_policies = True,
                order = -2147483648,
                policy_engine_mode = 'all',
                invalid_response_action = 'retry'
            )
        else:
            return FlowStageBindingRequest(
                target = '',
                stage = '',
                order = -2147483648,
        )
        """

    def testFlowStageBindingRequest(self):
        """Test FlowStageBindingRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
