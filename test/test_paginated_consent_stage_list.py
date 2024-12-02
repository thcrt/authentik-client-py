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

from authentik_client.models.paginated_consent_stage_list import PaginatedConsentStageList

class TestPaginatedConsentStageList(unittest.TestCase):
    """PaginatedConsentStageList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedConsentStageList:
        """Test PaginatedConsentStageList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedConsentStageList`
        """
        model = PaginatedConsentStageList()
        if include_optional:
            return PaginatedConsentStageList(
                pagination = authentik_client.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_client.models.consent_stage.ConsentStage(
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
                            ], 
                        mode = 'always_require', 
                        consent_expire_in = '', )
                    ]
            )
        else:
            return PaginatedConsentStageList(
                pagination = authentik_client.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_client.models.consent_stage.ConsentStage(
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
                            ], 
                        mode = 'always_require', 
                        consent_expire_in = '', )
                    ],
        )
        """

    def testPaginatedConsentStageList(self):
        """Test PaginatedConsentStageList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
