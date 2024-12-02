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

from authentik_client.models.invitation_stage_request import InvitationStageRequest

class TestInvitationStageRequest(unittest.TestCase):
    """InvitationStageRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvitationStageRequest:
        """Test InvitationStageRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvitationStageRequest`
        """
        model = InvitationStageRequest()
        if include_optional:
            return InvitationStageRequest(
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
                continue_flow_without_invitation = True
            )
        else:
            return InvitationStageRequest(
                name = '0',
        )
        """

    def testInvitationStageRequest(self):
        """Test InvitationStageRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
