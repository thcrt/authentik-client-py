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

from authentik_client.models.paginated_brand_list import PaginatedBrandList

class TestPaginatedBrandList(unittest.TestCase):
    """PaginatedBrandList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedBrandList:
        """Test PaginatedBrandList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedBrandList`
        """
        model = PaginatedBrandList()
        if include_optional:
            return PaginatedBrandList(
                pagination = authentik_client.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_client.models.brand.Brand(
                        brand_uuid = '', 
                        domain = '', 
                        default = True, 
                        branding_title = '', 
                        branding_logo = '', 
                        branding_favicon = '', 
                        flow_authentication = '', 
                        flow_invalidation = '', 
                        flow_recovery = '', 
                        flow_unenrollment = '', 
                        flow_user_settings = '', 
                        flow_device_code = '', 
                        default_application = '', 
                        web_certificate = '', 
                        attributes = null, )
                    ]
            )
        else:
            return PaginatedBrandList(
                pagination = authentik_client.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_client.models.brand.Brand(
                        brand_uuid = '', 
                        domain = '', 
                        default = True, 
                        branding_title = '', 
                        branding_logo = '', 
                        branding_favicon = '', 
                        flow_authentication = '', 
                        flow_invalidation = '', 
                        flow_recovery = '', 
                        flow_unenrollment = '', 
                        flow_user_settings = '', 
                        flow_device_code = '', 
                        default_application = '', 
                        web_certificate = '', 
                        attributes = null, )
                    ],
        )
        """

    def testPaginatedBrandList(self):
        """Test PaginatedBrandList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
