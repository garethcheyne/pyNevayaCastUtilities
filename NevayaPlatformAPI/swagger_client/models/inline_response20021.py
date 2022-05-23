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

class InlineResponse20021(object):
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
        'page': 'int',
        'count': 'int',
        'total_pages': 'int'
    }

    attribute_map = {
        'page': 'page',
        'count': 'count',
        'total_pages': 'total_pages'
    }

    def __init__(self, page=None, count=None, total_pages=None):  # noqa: E501
        """InlineResponse20021 - a model defined in Swagger"""  # noqa: E501
        self._page = None
        self._count = None
        self._total_pages = None
        self.discriminator = None
        if page is not None:
            self.page = page
        if count is not None:
            self.count = count
        if total_pages is not None:
            self.total_pages = total_pages

    @property
    def page(self):
        """Gets the page of this InlineResponse20021.  # noqa: E501

        The current page of the results  # noqa: E501

        :return: The page of this InlineResponse20021.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this InlineResponse20021.

        The current page of the results  # noqa: E501

        :param page: The page of this InlineResponse20021.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def count(self):
        """Gets the count of this InlineResponse20021.  # noqa: E501

        The total number of results available  # noqa: E501

        :return: The count of this InlineResponse20021.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this InlineResponse20021.

        The total number of results available  # noqa: E501

        :param count: The count of this InlineResponse20021.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def total_pages(self):
        """Gets the total_pages of this InlineResponse20021.  # noqa: E501

        The total number of pages available  # noqa: E501

        :return: The total_pages of this InlineResponse20021.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this InlineResponse20021.

        The total number of pages available  # noqa: E501

        :param total_pages: The total_pages of this InlineResponse20021.  # noqa: E501
        :type: int
        """

        self._total_pages = total_pages

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
        if issubclass(InlineResponse20021, dict):
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
        if not isinstance(other, InlineResponse20021):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
