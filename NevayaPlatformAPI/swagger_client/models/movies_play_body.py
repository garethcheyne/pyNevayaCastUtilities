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

class MoviesPlayBody(object):
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
        'language': 'str',
        'resume': 'bool',
        'movie_id': 'str',
        'receiver_id': 'str',
        'room_tag_id': 'str',
        'receiver_ids': 'list[str]'
    }

    attribute_map = {
        'language': 'language',
        'resume': 'resume',
        'movie_id': 'movie_id',
        'receiver_id': 'receiver_id',
        'room_tag_id': 'room_tag_id',
        'receiver_ids': 'receiver_ids'
    }

    def __init__(self, language=None, resume=None, movie_id=None, receiver_id=None, room_tag_id=None, receiver_ids=None):  # noqa: E501
        """MoviesPlayBody - a model defined in Swagger"""  # noqa: E501
        self._language = None
        self._resume = None
        self._movie_id = None
        self._receiver_id = None
        self._room_tag_id = None
        self._receiver_ids = None
        self.discriminator = None
        if language is not None:
            self.language = language
        if resume is not None:
            self.resume = resume
        self.movie_id = movie_id
        if receiver_id is not None:
            self.receiver_id = receiver_id
        if room_tag_id is not None:
            self.room_tag_id = room_tag_id
        if receiver_ids is not None:
            self.receiver_ids = receiver_ids

    @property
    def language(self):
        """Gets the language of this MoviesPlayBody.  # noqa: E501

        The ISO 639-1 code of the available movie languages  | Code   | Language     |                                  | |--------|--------------|----------------------------------| | en | English      |                                  | | fr | Français     |                                  | | es | Español      |                                  | | de | Deutsch      |                                  | | it | Italiano     |                                  | | un | Undetermined | _Generally this will be English_ | | nl | Nederlands   |                                  |  # noqa: E501

        :return: The language of this MoviesPlayBody.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this MoviesPlayBody.

        The ISO 639-1 code of the available movie languages  | Code   | Language     |                                  | |--------|--------------|----------------------------------| | en | English      |                                  | | fr | Français     |                                  | | es | Español      |                                  | | de | Deutsch      |                                  | | it | Italiano     |                                  | | un | Undetermined | _Generally this will be English_ | | nl | Nederlands   |                                  |  # noqa: E501

        :param language: The language of this MoviesPlayBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["en", "de", "fr", "es", "it", "nl", "un"]  # noqa: E501
        if language not in allowed_values:
            raise ValueError(
                "Invalid value for `language` ({0}), must be one of {1}"  # noqa: E501
                .format(language, allowed_values)
            )

        self._language = language

    @property
    def resume(self):
        """Gets the resume of this MoviesPlayBody.  # noqa: E501

        Restart the movie from the previous position if available  # noqa: E501

        :return: The resume of this MoviesPlayBody.  # noqa: E501
        :rtype: bool
        """
        return self._resume

    @resume.setter
    def resume(self, resume):
        """Sets the resume of this MoviesPlayBody.

        Restart the movie from the previous position if available  # noqa: E501

        :param resume: The resume of this MoviesPlayBody.  # noqa: E501
        :type: bool
        """

        self._resume = resume

    @property
    def movie_id(self):
        """Gets the movie_id of this MoviesPlayBody.  # noqa: E501

        The ID of the movie to be played  # noqa: E501

        :return: The movie_id of this MoviesPlayBody.  # noqa: E501
        :rtype: str
        """
        return self._movie_id

    @movie_id.setter
    def movie_id(self, movie_id):
        """Sets the movie_id of this MoviesPlayBody.

        The ID of the movie to be played  # noqa: E501

        :param movie_id: The movie_id of this MoviesPlayBody.  # noqa: E501
        :type: str
        """
        if movie_id is None:
            raise ValueError("Invalid value for `movie_id`, must not be `None`")  # noqa: E501

        self._movie_id = movie_id

    @property
    def receiver_id(self):
        """Gets the receiver_id of this MoviesPlayBody.  # noqa: E501

        The receiver ID  # noqa: E501

        :return: The receiver_id of this MoviesPlayBody.  # noqa: E501
        :rtype: str
        """
        return self._receiver_id

    @receiver_id.setter
    def receiver_id(self, receiver_id):
        """Sets the receiver_id of this MoviesPlayBody.

        The receiver ID  # noqa: E501

        :param receiver_id: The receiver_id of this MoviesPlayBody.  # noqa: E501
        :type: str
        """

        self._receiver_id = receiver_id

    @property
    def room_tag_id(self):
        """Gets the room_tag_id of this MoviesPlayBody.  # noqa: E501


        :return: The room_tag_id of this MoviesPlayBody.  # noqa: E501
        :rtype: str
        """
        return self._room_tag_id

    @room_tag_id.setter
    def room_tag_id(self, room_tag_id):
        """Sets the room_tag_id of this MoviesPlayBody.


        :param room_tag_id: The room_tag_id of this MoviesPlayBody.  # noqa: E501
        :type: str
        """

        self._room_tag_id = room_tag_id

    @property
    def receiver_ids(self):
        """Gets the receiver_ids of this MoviesPlayBody.  # noqa: E501

        Multiple receiver IDs  # noqa: E501

        :return: The receiver_ids of this MoviesPlayBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._receiver_ids

    @receiver_ids.setter
    def receiver_ids(self, receiver_ids):
        """Sets the receiver_ids of this MoviesPlayBody.

        Multiple receiver IDs  # noqa: E501

        :param receiver_ids: The receiver_ids of this MoviesPlayBody.  # noqa: E501
        :type: list[str]
        """

        self._receiver_ids = receiver_ids

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
        if issubclass(MoviesPlayBody, dict):
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
        if not isinstance(other, MoviesPlayBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
