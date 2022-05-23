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

class VideosPlayBody(object):
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
        'video_id': 'str',
        'receiver_id': 'str',
        'room_tag_id': 'str',
        'receiver_ids': 'list[str]'
    }

    attribute_map = {
        'video_id': 'video_id',
        'receiver_id': 'receiver_id',
        'room_tag_id': 'room_tag_id',
        'receiver_ids': 'receiver_ids'
    }

    def __init__(self, video_id=None, receiver_id=None, room_tag_id=None, receiver_ids=None):  # noqa: E501
        """VideosPlayBody - a model defined in Swagger"""  # noqa: E501
        self._video_id = None
        self._receiver_id = None
        self._room_tag_id = None
        self._receiver_ids = None
        self.discriminator = None
        self.video_id = video_id
        if receiver_id is not None:
            self.receiver_id = receiver_id
        if room_tag_id is not None:
            self.room_tag_id = room_tag_id
        if receiver_ids is not None:
            self.receiver_ids = receiver_ids

    @property
    def video_id(self):
        """Gets the video_id of this VideosPlayBody.  # noqa: E501

        The video ID  # noqa: E501

        :return: The video_id of this VideosPlayBody.  # noqa: E501
        :rtype: str
        """
        return self._video_id

    @video_id.setter
    def video_id(self, video_id):
        """Sets the video_id of this VideosPlayBody.

        The video ID  # noqa: E501

        :param video_id: The video_id of this VideosPlayBody.  # noqa: E501
        :type: str
        """
        if video_id is None:
            raise ValueError("Invalid value for `video_id`, must not be `None`")  # noqa: E501

        self._video_id = video_id

    @property
    def receiver_id(self):
        """Gets the receiver_id of this VideosPlayBody.  # noqa: E501

        The receiver ID  # noqa: E501

        :return: The receiver_id of this VideosPlayBody.  # noqa: E501
        :rtype: str
        """
        return self._receiver_id

    @receiver_id.setter
    def receiver_id(self, receiver_id):
        """Sets the receiver_id of this VideosPlayBody.

        The receiver ID  # noqa: E501

        :param receiver_id: The receiver_id of this VideosPlayBody.  # noqa: E501
        :type: str
        """

        self._receiver_id = receiver_id

    @property
    def room_tag_id(self):
        """Gets the room_tag_id of this VideosPlayBody.  # noqa: E501


        :return: The room_tag_id of this VideosPlayBody.  # noqa: E501
        :rtype: str
        """
        return self._room_tag_id

    @room_tag_id.setter
    def room_tag_id(self, room_tag_id):
        """Sets the room_tag_id of this VideosPlayBody.


        :param room_tag_id: The room_tag_id of this VideosPlayBody.  # noqa: E501
        :type: str
        """

        self._room_tag_id = room_tag_id

    @property
    def receiver_ids(self):
        """Gets the receiver_ids of this VideosPlayBody.  # noqa: E501

        Multiple receiver IDs  # noqa: E501

        :return: The receiver_ids of this VideosPlayBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._receiver_ids

    @receiver_ids.setter
    def receiver_ids(self, receiver_ids):
        """Sets the receiver_ids of this VideosPlayBody.

        Multiple receiver IDs  # noqa: E501

        :param receiver_ids: The receiver_ids of this VideosPlayBody.  # noqa: E501
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
        if issubclass(VideosPlayBody, dict):
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
        if not isinstance(other, VideosPlayBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
