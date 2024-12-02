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

from authentik_client.models.connection_token import ConnectionToken

class TestConnectionToken(unittest.TestCase):
    """ConnectionToken unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConnectionToken:
        """Test ConnectionToken
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConnectionToken`
        """
        model = ConnectionToken()
        if include_optional:
            return ConnectionToken(
                pk = '',
                provider = 56,
                provider_obj = authentik_client.models.rac_provider.RACProvider(
                    pk = 56, 
                    name = '', 
                    authentication_flow = '', 
                    authorization_flow = '', 
                    property_mappings = [
                        ''
                        ], 
                    component = '', 
                    assigned_application_slug = '', 
                    assigned_application_name = '', 
                    assigned_backchannel_application_slug = '', 
                    assigned_backchannel_application_name = '', 
                    verbose_name = '', 
                    verbose_name_plural = '', 
                    meta_model_name = '', 
                    settings = null, 
                    outpost_set = [
                        ''
                        ], 
                    connection_expiry = '', 
                    delete_token_on_disconnect = True, ),
                endpoint = '',
                endpoint_obj = authentik_client.models.endpoint.Endpoint(
                    pk = '', 
                    name = '', 
                    provider = 56, 
                    provider_obj = null, 
                    protocol = 'rdp', 
                    host = '', 
                    settings = null, 
                    property_mappings = [
                        ''
                        ], 
                    auth_mode = 'static', 
                    launch_url = '', 
                    maximum_connections = -2147483648, ),
                user = authentik_client.models.group_member.GroupMember(
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
            )
        else:
            return ConnectionToken(
                provider = 56,
                provider_obj = authentik_client.models.rac_provider.RACProvider(
                    pk = 56, 
                    name = '', 
                    authentication_flow = '', 
                    authorization_flow = '', 
                    property_mappings = [
                        ''
                        ], 
                    component = '', 
                    assigned_application_slug = '', 
                    assigned_application_name = '', 
                    assigned_backchannel_application_slug = '', 
                    assigned_backchannel_application_name = '', 
                    verbose_name = '', 
                    verbose_name_plural = '', 
                    meta_model_name = '', 
                    settings = null, 
                    outpost_set = [
                        ''
                        ], 
                    connection_expiry = '', 
                    delete_token_on_disconnect = True, ),
                endpoint = '',
                endpoint_obj = authentik_client.models.endpoint.Endpoint(
                    pk = '', 
                    name = '', 
                    provider = 56, 
                    provider_obj = null, 
                    protocol = 'rdp', 
                    host = '', 
                    settings = null, 
                    property_mappings = [
                        ''
                        ], 
                    auth_mode = 'static', 
                    launch_url = '', 
                    maximum_connections = -2147483648, ),
                user = authentik_client.models.group_member.GroupMember(
                    pk = 56, 
                    username = 'A', 
                    name = '', 
                    is_active = True, 
                    last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    email = '', 
                    attributes = {
                        'key' : null
                        }, 
                    uid = '', ),
        )
        """

    def testConnectionToken(self):
        """Test ConnectionToken"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
