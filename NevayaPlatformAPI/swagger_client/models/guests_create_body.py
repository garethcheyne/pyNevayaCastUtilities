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

class GuestsCreateBody(object):
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
        'locale': 'str'
    }

    attribute_map = {
        'locale': 'locale'
    }

    def __init__(self, locale=None):  # noqa: E501
        """GuestsCreateBody - a model defined in Swagger"""  # noqa: E501
        self._locale = None
        self.discriminator = None
        if locale is not None:
            self.locale = locale

    @property
    def locale(self):
        """Gets the locale of this GuestsCreateBody.  # noqa: E501

        ISO 639-1 language code. Currently the following are supported:  | Code  | Language           | |-------|--------------------| | en    | English (UK)       | | fr    | French             | | es    | Spanish            | | de    | German             | | zh-CN | Simplified Chinese | | en-US | English (US)       | | ar    | Arabic             |  # noqa: E501

        :return: The locale of this GuestsCreateBody.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this GuestsCreateBody.

        ISO 639-1 language code. Currently the following are supported:  | Code  | Language           | |-------|--------------------| | en    | English (UK)       | | fr    | French             | | es    | Spanish            | | de    | German             | | zh-CN | Simplified Chinese | | en-US | English (US)       | | ar    | Arabic             |  # noqa: E501

        :param locale: The locale of this GuestsCreateBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["en", "de", "fr", "es", "en-US", "ar", "zh-CN"]  # noqa: E501
        if locale not in allowed_values:
            raise ValueError(
                "Invalid value for `locale` ({0}), must be one of {1}"  # noqa: E501
                .format(locale, allowed_values)
            )

        self._locale = locale

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
        if issubclass(GuestsCreateBody, dict):
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
        if not isinstance(other, GuestsCreateBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
