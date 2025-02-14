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

from authentik_client.models.paginated_saml_source_list import PaginatedSAMLSourceList

class TestPaginatedSAMLSourceList(unittest.TestCase):
    """PaginatedSAMLSourceList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedSAMLSourceList:
        """Test PaginatedSAMLSourceList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedSAMLSourceList`
        """
        model = PaginatedSAMLSourceList()
        if include_optional:
            return PaginatedSAMLSourceList(
                pagination = authentik_client.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_client.models.saml_source.SAMLSource(
                        pk = '', 
                        name = '', 
                        slug = 'z', 
                        enabled = True, 
                        authentication_flow = '', 
                        enrollment_flow = '', 
                        user_property_mappings = [
                            ''
                            ], 
                        group_property_mappings = [
                            ''
                            ], 
                        component = '', 
                        verbose_name = '', 
                        verbose_name_plural = '', 
                        meta_model_name = '', 
                        policy_engine_mode = 'all', 
                        user_matching_mode = null, 
                        managed = '', 
                        user_path_template = '', 
                        icon = '', 
                        group_matching_mode = null, 
                        pre_authentication_flow = '', 
                        issuer = '', 
                        sso_url = '', 
                        slo_url = '', 
                        allow_idp_initiated = True, 
                        name_id_policy = null, 
                        binding_type = 'REDIRECT', 
                        verification_kp = '', 
                        signing_kp = '', 
                        digest_algorithm = 'http://www.w3.org/2000/09/xmldsig#sha1', 
                        signature_algorithm = 'http://www.w3.org/2000/09/xmldsig#rsa-sha1', 
                        temporary_user_delete_after = '', 
                        encryption_kp = '', )
                    ]
            )
        else:
            return PaginatedSAMLSourceList(
                pagination = authentik_client.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_client.models.saml_source.SAMLSource(
                        pk = '', 
                        name = '', 
                        slug = 'z', 
                        enabled = True, 
                        authentication_flow = '', 
                        enrollment_flow = '', 
                        user_property_mappings = [
                            ''
                            ], 
                        group_property_mappings = [
                            ''
                            ], 
                        component = '', 
                        verbose_name = '', 
                        verbose_name_plural = '', 
                        meta_model_name = '', 
                        policy_engine_mode = 'all', 
                        user_matching_mode = null, 
                        managed = '', 
                        user_path_template = '', 
                        icon = '', 
                        group_matching_mode = null, 
                        pre_authentication_flow = '', 
                        issuer = '', 
                        sso_url = '', 
                        slo_url = '', 
                        allow_idp_initiated = True, 
                        name_id_policy = null, 
                        binding_type = 'REDIRECT', 
                        verification_kp = '', 
                        signing_kp = '', 
                        digest_algorithm = 'http://www.w3.org/2000/09/xmldsig#sha1', 
                        signature_algorithm = 'http://www.w3.org/2000/09/xmldsig#rsa-sha1', 
                        temporary_user_delete_after = '', 
                        encryption_kp = '', )
                    ],
        )
        """

    def testPaginatedSAMLSourceList(self):
        """Test PaginatedSAMLSourceList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
