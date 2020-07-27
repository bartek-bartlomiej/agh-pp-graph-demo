# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.any_value import AnyValue  # noqa: F401,E501
from swagger_server import util


class Parameter(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, value: AnyValue=None):  # noqa: E501
        """Parameter - a model defined in Swagger

        :param name: The name of this Parameter.  # noqa: E501
        :type name: str
        :param value: The value of this Parameter.  # noqa: E501
        :type value: AnyValue
        """
        self.swagger_types = {
            'name': str,
            'value': AnyValue
        }

        self.attribute_map = {
            'name': 'name',
            'value': 'value'
        }
        self._name = name
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'Parameter':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Parameter of this Parameter.  # noqa: E501
        :rtype: Parameter
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this Parameter.


        :return: The name of this Parameter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Parameter.


        :param name: The name of this Parameter.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def value(self) -> AnyValue:
        """Gets the value of this Parameter.


        :return: The value of this Parameter.
        :rtype: AnyValue
        """
        return self._value

    @value.setter
    def value(self, value: AnyValue):
        """Sets the value of this Parameter.


        :param value: The value of this Parameter.
        :type value: AnyValue
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value
