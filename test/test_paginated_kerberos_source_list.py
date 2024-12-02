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

from authentik_client.models.paginated_kerberos_source_list import PaginatedKerberosSourceList

class TestPaginatedKerberosSourceList(unittest.TestCase):
    """PaginatedKerberosSourceList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedKerberosSourceList:
        """Test PaginatedKerberosSourceList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedKerberosSourceList`
        """
        model = PaginatedKerberosSourceList()
        if include_optional:
            return PaginatedKerberosSourceList(
                pagination = authentik_client.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_client.models.kerberos_source.KerberosSource(
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
                        realm = '', 
                        krb5_conf = '', 
                        sync_users = True, 
                        sync_users_password = True, 
                        sync_principal = '', 
                        sync_ccache = '', 
                        connectivity = {
                            'key' : ''
                            }, 
                        spnego_server_name = '', 
                        spnego_ccache = '', 
                        password_login_update_internal_password = True, )
                    ]
            )
        else:
            return PaginatedKerberosSourceList(
                pagination = authentik_client.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_client.models.kerberos_source.KerberosSource(
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
                        realm = '', 
                        krb5_conf = '', 
                        sync_users = True, 
                        sync_users_password = True, 
                        sync_principal = '', 
                        sync_ccache = '', 
                        connectivity = {
                            'key' : ''
                            }, 
                        spnego_server_name = '', 
                        spnego_ccache = '', 
                        password_login_update_internal_password = True, )
                    ],
        )
        """

    def testPaginatedKerberosSourceList(self):
        """Test PaginatedKerberosSourceList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
