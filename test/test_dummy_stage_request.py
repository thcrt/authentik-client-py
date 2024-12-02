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

from authentik_client.models.dummy_stage_request import DummyStageRequest

class TestDummyStageRequest(unittest.TestCase):
    """DummyStageRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DummyStageRequest:
        """Test DummyStageRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DummyStageRequest`
        """
        model = DummyStageRequest()
        if include_optional:
            return DummyStageRequest(
                name = '0',
                flow_set = [
                    authentik_client.models.flow_set_request.FlowSetRequest(
                        name = '0', 
                        slug = 'z0', 
                        title = '0', 
                        designation = null, 
                        policy_engine_mode = 'all', 
                        compatibility_mode = True, 
                        layout = 'stacked', 
                        denied_action = null, )
                    ],
                throw_error = True
            )
        else:
            return DummyStageRequest(
                name = '0',
        )
        """

    def testDummyStageRequest(self):
        """Test DummyStageRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
