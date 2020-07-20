# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class NodePosition(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, x: float=None, y: float=None):  # noqa: E501
        """NodePosition - a model defined in Swagger

        :param id: The id of this NodePosition.  # noqa: E501
        :type id: str
        :param x: The x of this NodePosition.  # noqa: E501
        :type x: float
        :param y: The y of this NodePosition.  # noqa: E501
        :type y: float
        """
        self.swagger_types = {
            'id': str,
            'x': float,
            'y': float
        }

        self.attribute_map = {
            'id': 'id',
            'x': 'x',
            'y': 'y'
        }
        self._id = id
        self._x = x
        self._y = y

    @classmethod
    def from_dict(cls, dikt) -> 'NodePosition':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NodePosition of this NodePosition.  # noqa: E501
        :rtype: NodePosition
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this NodePosition.


        :return: The id of this NodePosition.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this NodePosition.


        :param id: The id of this NodePosition.
        :type id: str
        """

        self._id = id

    @property
    def x(self) -> float:
        """Gets the x of this NodePosition.


        :return: The x of this NodePosition.
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x: float):
        """Sets the x of this NodePosition.


        :param x: The x of this NodePosition.
        :type x: float
        """

        self._x = x

    @property
    def y(self) -> float:
        """Gets the y of this NodePosition.


        :return: The y of this NodePosition.
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y: float):
        """Sets the y of this NodePosition.


        :param y: The y of this NodePosition.
        :type y: float
        """

        self._y = y
