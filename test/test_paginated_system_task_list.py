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

from authentik_client.models.paginated_system_task_list import PaginatedSystemTaskList

class TestPaginatedSystemTaskList(unittest.TestCase):
    """PaginatedSystemTaskList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedSystemTaskList:
        """Test PaginatedSystemTaskList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedSystemTaskList`
        """
        model = PaginatedSystemTaskList()
        if include_optional:
            return PaginatedSystemTaskList(
                pagination = authentik_client.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_client.models.system_task.SystemTask(
                        uuid = '', 
                        name = '', 
                        full_name = '', 
                        uid = '', 
                        description = '', 
                        start_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        finish_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        duration = 1.337, 
                        status = 'unknown', 
                        messages = [
                            authentik_client.models.log_event.LogEvent(
                                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                log_level = 'critical', 
                                logger = '', 
                                event = '', 
                                attributes = {
                                    'key' : null
                                    }, )
                            ], 
                        expires = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        expiring = True, )
                    ]
            )
        else:
            return PaginatedSystemTaskList(
                pagination = authentik_client.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_client.models.system_task.SystemTask(
                        uuid = '', 
                        name = '', 
                        full_name = '', 
                        uid = '', 
                        description = '', 
                        start_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        finish_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        duration = 1.337, 
                        status = 'unknown', 
                        messages = [
                            authentik_client.models.log_event.LogEvent(
                                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                log_level = 'critical', 
                                logger = '', 
                                event = '', 
                                attributes = {
                                    'key' : null
                                    }, )
                            ], 
                        expires = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        expiring = True, )
                    ],
        )
        """

    def testPaginatedSystemTaskList(self):
        """Test PaginatedSystemTaskList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
