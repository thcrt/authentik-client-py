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

from authentik_client.models.policy_binding import PolicyBinding

class TestPolicyBinding(unittest.TestCase):
    """PolicyBinding unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PolicyBinding:
        """Test PolicyBinding
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PolicyBinding`
        """
        model = PolicyBinding()
        if include_optional:
            return PolicyBinding(
                pk = '',
                policy = '',
                group = '',
                user = 56,
                policy_obj = authentik_client.models.policy.Policy(
                    pk = '', 
                    name = '', 
                    execution_logging = True, 
                    component = '', 
                    verbose_name = '', 
                    verbose_name_plural = '', 
                    meta_model_name = '', 
                    bound_to = 56, ),
                group_obj = authentik_client.models.group.Group(
                    pk = '', 
                    num_pk = 56, 
                    name = '', 
                    is_superuser = True, 
                    parent = '', 
                    parent_name = '', 
                    users = [
                        56
                        ], 
                    users_obj = [
                        authentik_client.models.group_member.GroupMember(
                            pk = 56, 
                            username = 'A', 
                            name = '', 
                            is_active = True, 
                            last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            email = '', 
                            attributes = {
                                'key' : null
                                }, 
                            uid = '', )
                        ], 
                    attributes = {
                        'key' : null
                        }, 
                    roles = [
                        ''
                        ], 
                    roles_obj = [
                        authentik_client.models.role.Role(
                            pk = '', 
                            name = '', )
                        ], ),
                user_obj = authentik_client.models.user.User(
                    pk = 56, 
                    username = '', 
                    name = '', 
                    is_active = True, 
                    last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    is_superuser = True, 
                    groups = [
                        ''
                        ], 
                    groups_obj = [
                        authentik_client.models.user_group.UserGroup(
                            pk = '', 
                            num_pk = 56, 
                            name = '', 
                            is_superuser = True, 
                            parent = '', 
                            parent_name = '', 
                            attributes = {
                                'key' : null
                                }, )
                        ], 
                    email = '', 
                    avatar = '', 
                    attributes = {
                        'key' : null
                        }, 
                    uid = '', 
                    path = '', 
                    type = 'internal', 
                    uuid = '', ),
                target = '',
                negate = True,
                enabled = True,
                order = -2147483648,
                timeout = 0,
                failure_result = True
            )
        else:
            return PolicyBinding(
                pk = '',
                policy_obj = authentik_client.models.policy.Policy(
                    pk = '', 
                    name = '', 
                    execution_logging = True, 
                    component = '', 
                    verbose_name = '', 
                    verbose_name_plural = '', 
                    meta_model_name = '', 
                    bound_to = 56, ),
                group_obj = authentik_client.models.group.Group(
                    pk = '', 
                    num_pk = 56, 
                    name = '', 
                    is_superuser = True, 
                    parent = '', 
                    parent_name = '', 
                    users = [
                        56
                        ], 
                    users_obj = [
                        authentik_client.models.group_member.GroupMember(
                            pk = 56, 
                            username = 'A', 
                            name = '', 
                            is_active = True, 
                            last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            email = '', 
                            attributes = {
                                'key' : null
                                }, 
                            uid = '', )
                        ], 
                    attributes = {
                        'key' : null
                        }, 
                    roles = [
                        ''
                        ], 
                    roles_obj = [
                        authentik_client.models.role.Role(
                            pk = '', 
                            name = '', )
                        ], ),
                user_obj = authentik_client.models.user.User(
                    pk = 56, 
                    username = '', 
                    name = '', 
                    is_active = True, 
                    last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    is_superuser = True, 
                    groups = [
                        ''
                        ], 
                    groups_obj = [
                        authentik_client.models.user_group.UserGroup(
                            pk = '', 
                            num_pk = 56, 
                            name = '', 
                            is_superuser = True, 
                            parent = '', 
                            parent_name = '', 
                            attributes = {
                                'key' : null
                                }, )
                        ], 
                    email = '', 
                    avatar = '', 
                    attributes = {
                        'key' : null
                        }, 
                    uid = '', 
                    path = '', 
                    type = 'internal', 
                    uuid = '', ),
                target = '',
                order = -2147483648,
        )
        """

    def testPolicyBinding(self):
        """Test PolicyBinding"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
