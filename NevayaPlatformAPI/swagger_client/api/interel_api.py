# coding: utf-8

"""
    Nevaya Platform

    Access to everything Nevaya  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: contact@nevaya.co.uk
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class InterelApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_room_control_interel_state(self, room_id, **kwargs):  # noqa: E501
        """Get the Interel room state  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_room_control_interel_state(room_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str room_id: The room ID (required)
        :return: InlineResponse20022
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_room_control_interel_state_with_http_info(room_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_room_control_interel_state_with_http_info(room_id, **kwargs)  # noqa: E501
            return data

    def get_room_control_interel_state_with_http_info(self, room_id, **kwargs):  # noqa: E501
        """Get the Interel room state  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_room_control_interel_state_with_http_info(room_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str room_id: The room ID (required)
        :return: InlineResponse20022
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['room_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_room_control_interel_state" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'room_id' is set
        if ('room_id' not in params or
                params['room_id'] is None):
            raise ValueError("Missing the required parameter `room_id` when calling `get_room_control_interel_state`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'room_id' in params:
            query_params.append(('room_id', params['room_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/room-control/interel/state', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20022',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_room_control_interel_set_blind_state(self, **kwargs):  # noqa: E501
        """Control the blinds in the room  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_room_control_interel_set_blind_state(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InterelSetblindstateBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_room_control_interel_set_blind_state_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_room_control_interel_set_blind_state_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_room_control_interel_set_blind_state_with_http_info(self, **kwargs):  # noqa: E501
        """Control the blinds in the room  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_room_control_interel_set_blind_state_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InterelSetblindstateBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_room_control_interel_set_blind_state" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/room-control/interel/set-blind-state', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_room_control_interel_set_curtain_state(self, **kwargs):  # noqa: E501
        """Control the curtains in the room  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_room_control_interel_set_curtain_state(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InterelSetcurtainstateBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_room_control_interel_set_curtain_state_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_room_control_interel_set_curtain_state_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_room_control_interel_set_curtain_state_with_http_info(self, **kwargs):  # noqa: E501
        """Control the curtains in the room  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_room_control_interel_set_curtain_state_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InterelSetcurtainstateBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_room_control_interel_set_curtain_state" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/room-control/interel/set-curtain-state', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_room_control_interel_set_dnd_state(self, **kwargs):  # noqa: E501
        """Set the do not disturb state for the room  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_room_control_interel_set_dnd_state(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InterelSetdndstateBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_room_control_interel_set_dnd_state_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_room_control_interel_set_dnd_state_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_room_control_interel_set_dnd_state_with_http_info(self, **kwargs):  # noqa: E501
        """Set the do not disturb state for the room  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_room_control_interel_set_dnd_state_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InterelSetdndstateBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_room_control_interel_set_dnd_state" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/room-control/interel/set-dnd-state', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_room_control_interel_set_fan_speed(self, **kwargs):  # noqa: E501
        """Set the fan speed for the room  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_room_control_interel_set_fan_speed(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InterelSetfanspeedBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_room_control_interel_set_fan_speed_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_room_control_interel_set_fan_speed_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_room_control_interel_set_fan_speed_with_http_info(self, **kwargs):  # noqa: E501
        """Set the fan speed for the room  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_room_control_interel_set_fan_speed_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InterelSetfanspeedBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_room_control_interel_set_fan_speed" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/room-control/interel/set-fan-speed', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_room_control_interel_set_scene(self, **kwargs):  # noqa: E501
        """Set a scene  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_room_control_interel_set_scene(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InterelSetsceneBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_room_control_interel_set_scene_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_room_control_interel_set_scene_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_room_control_interel_set_scene_with_http_info(self, **kwargs):  # noqa: E501
        """Set a scene  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_room_control_interel_set_scene_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InterelSetsceneBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_room_control_interel_set_scene" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/room-control/interel/set-scene', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_room_control_interel_set_temperature(self, **kwargs):  # noqa: E501
        """Set the temperature of a thermostat in the room  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_room_control_interel_set_temperature(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InterelSettemperatureBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_room_control_interel_set_temperature_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_room_control_interel_set_temperature_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_room_control_interel_set_temperature_with_http_info(self, **kwargs):  # noqa: E501
        """Set the temperature of a thermostat in the room  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_room_control_interel_set_temperature_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InterelSettemperatureBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_room_control_interel_set_temperature" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/room-control/interel/set-temperature', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_room_control_interel_toggle_light(self, **kwargs):  # noqa: E501
        """Toggle a light  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_room_control_interel_toggle_light(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InterelTogglelightBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_room_control_interel_toggle_light_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_room_control_interel_toggle_light_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_room_control_interel_toggle_light_with_http_info(self, **kwargs):  # noqa: E501
        """Toggle a light  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_room_control_interel_toggle_light_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InterelTogglelightBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_room_control_interel_toggle_light" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/room-control/interel/toggle-light', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
