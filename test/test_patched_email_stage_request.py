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

from authentik_client.models.patched_email_stage_request import PatchedEmailStageRequest

class TestPatchedEmailStageRequest(unittest.TestCase):
    """PatchedEmailStageRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedEmailStageRequest:
        """Test PatchedEmailStageRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedEmailStageRequest`
        """
        model = PatchedEmailStageRequest()
        if include_optional:
            return PatchedEmailStageRequest(
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
                use_global_settings = True,
                host = '0',
                port = -2147483648,
                username = '',
                password = '',
                use_tls = True,
                use_ssl = True,
                timeout = -2147483648,
                from_address = '0',
                token_expiry = -2147483648,
                subject = '0',
                template = '0',
                activate_user_on_success = True
            )
        else:
            return PatchedEmailStageRequest(
        )
        """

    def testPatchedEmailStageRequest(self):
        """Test PatchedEmailStageRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
