# coding: utf-8

"""
    Nevaya Platform

    Access to everything Nevaya  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: contact@nevaya.co.uk
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InterelTogglelightBody(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'room_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'room_id': 'room_id'
    }

    def __init__(self, id=None, room_id=None):  # noqa: E501
        """InterelTogglelightBody - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._room_id = None
        self.discriminator = None
        self.id = id
        self.room_id = room_id

    @property
    def id(self):
        """Gets the id of this InterelTogglelightBody.  # noqa: E501


        :return: The id of this InterelTogglelightBody.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InterelTogglelightBody.


        :param id: The id of this InterelTogglelightBody.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def room_id(self):
        """Gets the room_id of this InterelTogglelightBody.  # noqa: E501

        The room ID  # noqa: E501

        :return: The room_id of this InterelTogglelightBody.  # noqa: E501
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this InterelTogglelightBody.

        The room ID  # noqa: E501

        :param room_id: The room_id of this InterelTogglelightBody.  # noqa: E501
        :type: str
        """
        if room_id is None:
            raise ValueError("Invalid value for `room_id`, must not be `None`")  # noqa: E501

        self._room_id = room_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InterelTogglelightBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InterelTogglelightBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
