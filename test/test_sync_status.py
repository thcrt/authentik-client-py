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

from authentik_client.models.sync_status import SyncStatus

class TestSyncStatus(unittest.TestCase):
    """SyncStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SyncStatus:
        """Test SyncStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SyncStatus`
        """
        model = SyncStatus()
        if include_optional:
            return SyncStatus(
                is_running = True,
                tasks = [
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
            return SyncStatus(
                is_running = True,
                tasks = [
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

    def testSyncStatus(self):
        """Test SyncStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
