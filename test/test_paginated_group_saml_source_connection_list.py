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

from authentik_client.models.paginated_group_saml_source_connection_list import PaginatedGroupSAMLSourceConnectionList

class TestPaginatedGroupSAMLSourceConnectionList(unittest.TestCase):
    """PaginatedGroupSAMLSourceConnectionList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedGroupSAMLSourceConnectionList:
        """Test PaginatedGroupSAMLSourceConnectionList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedGroupSAMLSourceConnectionList`
        """
        model = PaginatedGroupSAMLSourceConnectionList()
        if include_optional:
            return PaginatedGroupSAMLSourceConnectionList(
                pagination = authentik_client.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_client.models.group_saml_source_connection.GroupSAMLSourceConnection(
                        pk = 56, 
                        group = '', 
                        source = null, 
                        identifier = '', 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return PaginatedGroupSAMLSourceConnectionList(
                pagination = authentik_client.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_client.models.group_saml_source_connection.GroupSAMLSourceConnection(
                        pk = 56, 
                        group = '', 
                        source = null, 
                        identifier = '', 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
        )
        """

    def testPaginatedGroupSAMLSourceConnectionList(self):
        """Test PaginatedGroupSAMLSourceConnectionList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
