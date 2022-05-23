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

class MoviesResponse(object):
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
        'movies': 'list[Movie]',
        'genres': 'list[MovieGenre]',
        'sub_genres': 'list[MovieSubGenre]'
    }

    attribute_map = {
        'movies': 'movies',
        'genres': 'genres',
        'sub_genres': 'sub_genres'
    }

    def __init__(self, movies=None, genres=None, sub_genres=None):  # noqa: E501
        """MoviesResponse - a model defined in Swagger"""  # noqa: E501
        self._movies = None
        self._genres = None
        self._sub_genres = None
        self.discriminator = None
        if movies is not None:
            self.movies = movies
        if genres is not None:
            self.genres = genres
        if sub_genres is not None:
            self.sub_genres = sub_genres

    @property
    def movies(self):
        """Gets the movies of this MoviesResponse.  # noqa: E501


        :return: The movies of this MoviesResponse.  # noqa: E501
        :rtype: list[Movie]
        """
        return self._movies

    @movies.setter
    def movies(self, movies):
        """Sets the movies of this MoviesResponse.


        :param movies: The movies of this MoviesResponse.  # noqa: E501
        :type: list[Movie]
        """

        self._movies = movies

    @property
    def genres(self):
        """Gets the genres of this MoviesResponse.  # noqa: E501


        :return: The genres of this MoviesResponse.  # noqa: E501
        :rtype: list[MovieGenre]
        """
        return self._genres

    @genres.setter
    def genres(self, genres):
        """Sets the genres of this MoviesResponse.


        :param genres: The genres of this MoviesResponse.  # noqa: E501
        :type: list[MovieGenre]
        """

        self._genres = genres

    @property
    def sub_genres(self):
        """Gets the sub_genres of this MoviesResponse.  # noqa: E501


        :return: The sub_genres of this MoviesResponse.  # noqa: E501
        :rtype: list[MovieSubGenre]
        """
        return self._sub_genres

    @sub_genres.setter
    def sub_genres(self, sub_genres):
        """Sets the sub_genres of this MoviesResponse.


        :param sub_genres: The sub_genres of this MoviesResponse.  # noqa: E501
        :type: list[MovieSubGenre]
        """

        self._sub_genres = sub_genres

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
        if issubclass(MoviesResponse, dict):
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
        if not isinstance(other, MoviesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
