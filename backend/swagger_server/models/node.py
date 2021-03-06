# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.node_data import NodeData  # noqa: F401,E501
from swagger_server import util


class Node(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, data: NodeData=None):  # noqa: E501
        """Node - a model defined in Swagger

        :param data: The data of this Node.  # noqa: E501
        :type data: NodeData
        """
        self.swagger_types = {
            'data': NodeData
        }

        self.attribute_map = {
            'data': 'data'
        }
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'Node':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Node of this Node.  # noqa: E501
        :rtype: Node
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self) -> NodeData:
        """Gets the data of this Node.


        :return: The data of this Node.
        :rtype: NodeData
        """
        return self._data

    @data.setter
    def data(self, data: NodeData):
        """Sets the data of this Node.


        :param data: The data of this Node.
        :type data: NodeData
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data
