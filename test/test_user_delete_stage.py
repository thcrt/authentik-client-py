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

from authentik_client.models.user_delete_stage import UserDeleteStage

class TestUserDeleteStage(unittest.TestCase):
    """UserDeleteStage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserDeleteStage:
        """Test UserDeleteStage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserDeleteStage`
        """
        model = UserDeleteStage()
        if include_optional:
            return UserDeleteStage(
                pk = '',
                name = '',
                component = '',
                verbose_name = '',
                verbose_name_plural = '',
                meta_model_name = '',
                flow_set = [
                    authentik_client.models.flow_set.FlowSet(
                        pk = '', 
                        policybindingmodel_ptr_id = '', 
                        name = '', 
                        slug = 'z', 
                        title = '', 
                        designation = null, 
                        background = '', 
                        policy_engine_mode = 'all', 
                        compatibility_mode = True, 
                        export_url = '', 
                        layout = 'stacked', 
                        denied_action = null, )
                    ]
            )
        else:
            return UserDeleteStage(
                pk = '',
                name = '',
                component = '',
                verbose_name = '',
                verbose_name_plural = '',
                meta_model_name = '',
        )
        """

    def testUserDeleteStage(self):
        """Test UserDeleteStage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
