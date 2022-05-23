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

class AllWeatherCurrentWeather(object):
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
        'id': 'int',
        'main': 'str',
        'description': 'str',
        'icon': 'str'
    }

    attribute_map = {
        'id': 'id',
        'main': 'main',
        'description': 'description',
        'icon': 'icon'
    }

    def __init__(self, id=None, main=None, description=None, icon=None):  # noqa: E501
        """AllWeatherCurrentWeather - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._main = None
        self._description = None
        self._icon = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if main is not None:
            self.main = main
        if description is not None:
            self.description = description
        if icon is not None:
            self.icon = icon

    @property
    def id(self):
        """Gets the id of this AllWeatherCurrentWeather.  # noqa: E501

        Weather condition id  # noqa: E501

        :return: The id of this AllWeatherCurrentWeather.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AllWeatherCurrentWeather.

        Weather condition id  # noqa: E501

        :param id: The id of this AllWeatherCurrentWeather.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def main(self):
        """Gets the main of this AllWeatherCurrentWeather.  # noqa: E501

        Group of weather parameters (Rain, Snow, Extreme etc.)  # noqa: E501

        :return: The main of this AllWeatherCurrentWeather.  # noqa: E501
        :rtype: str
        """
        return self._main

    @main.setter
    def main(self, main):
        """Sets the main of this AllWeatherCurrentWeather.

        Group of weather parameters (Rain, Snow, Extreme etc.)  # noqa: E501

        :param main: The main of this AllWeatherCurrentWeather.  # noqa: E501
        :type: str
        """

        self._main = main

    @property
    def description(self):
        """Gets the description of this AllWeatherCurrentWeather.  # noqa: E501

        Weather condition within the group  # noqa: E501

        :return: The description of this AllWeatherCurrentWeather.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AllWeatherCurrentWeather.

        Weather condition within the group  # noqa: E501

        :param description: The description of this AllWeatherCurrentWeather.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def icon(self):
        """Gets the icon of this AllWeatherCurrentWeather.  # noqa: E501

        Weather icon ID  # noqa: E501

        :return: The icon of this AllWeatherCurrentWeather.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this AllWeatherCurrentWeather.

        Weather icon ID  # noqa: E501

        :param icon: The icon of this AllWeatherCurrentWeather.  # noqa: E501
        :type: str
        """

        self._icon = icon

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
        if issubclass(AllWeatherCurrentWeather, dict):
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
        if not isinstance(other, AllWeatherCurrentWeather):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
