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

from authentik_client.models.frame_challenge import FrameChallenge

class TestFrameChallenge(unittest.TestCase):
    """FrameChallenge unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FrameChallenge:
        """Test FrameChallenge
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FrameChallenge`
        """
        model = FrameChallenge()
        if include_optional:
            return FrameChallenge(
                flow_info = authentik_client.models.contextual_flow_info.ContextualFlowInfo(
                    title = '', 
                    background = '', 
                    cancel_url = '', 
                    layout = 'stacked', ),
                component = 'xak-flow-frame',
                response_errors = {
                    'key' : [
                        authentik_client.models.error_detail.ErrorDetail(
                            string = '', 
                            code = '', )
                        ]
                    },
                url = '',
                loading_overlay = True,
                loading_text = ''
            )
        else:
            return FrameChallenge(
                url = '',
                loading_text = '',
        )
        """

    def testFrameChallenge(self):
        """Test FrameChallenge"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
