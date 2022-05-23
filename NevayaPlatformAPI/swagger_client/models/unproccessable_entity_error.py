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

class UnproccessableEntityError(object):
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
        'type': 'str',
        'message': 'str',
        'status': 'int',
        'errors': 'list[UnproccessableEntityErrorErrors]'
    }

    attribute_map = {
        'type': 'type',
        'message': 'message',
        'status': 'status',
        'errors': 'errors'
    }

    def __init__(self, type='Unprocessable Entity', message=None, status=422, errors=None):  # noqa: E501
        """UnproccessableEntityError - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._message = None
        self._status = None
        self._errors = None
        self.discriminator = None
        self.type = type
        self.message = message
        self.status = status
        if errors is not None:
            self.errors = errors

    @property
    def type(self):
        """Gets the type of this UnproccessableEntityError.  # noqa: E501


        :return: The type of this UnproccessableEntityError.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UnproccessableEntityError.


        :param type: The type of this UnproccessableEntityError.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def message(self):
        """Gets the message of this UnproccessableEntityError.  # noqa: E501


        :return: The message of this UnproccessableEntityError.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this UnproccessableEntityError.


        :param message: The message of this UnproccessableEntityError.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def status(self):
        """Gets the status of this UnproccessableEntityError.  # noqa: E501


        :return: The status of this UnproccessableEntityError.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UnproccessableEntityError.


        :param status: The status of this UnproccessableEntityError.  # noqa: E501
        :type: int
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def errors(self):
        """Gets the errors of this UnproccessableEntityError.  # noqa: E501


        :return: The errors of this UnproccessableEntityError.  # noqa: E501
        :rtype: list[UnproccessableEntityErrorErrors]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this UnproccessableEntityError.


        :param errors: The errors of this UnproccessableEntityError.  # noqa: E501
        :type: list[UnproccessableEntityErrorErrors]
        """

        self._errors = errors

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
        if issubclass(UnproccessableEntityError, dict):
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
        if not isinstance(other, UnproccessableEntityError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
