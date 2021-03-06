# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.graph_elements import GraphElements  # noqa: F401,E501
from swagger_server import util


class Graph(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, directed: bool=None, multigraph: bool=None, elements: GraphElements=None):  # noqa: E501
        """Graph - a model defined in Swagger

        :param directed: The directed of this Graph.  # noqa: E501
        :type directed: bool
        :param multigraph: The multigraph of this Graph.  # noqa: E501
        :type multigraph: bool
        :param elements: The elements of this Graph.  # noqa: E501
        :type elements: GraphElements
        """
        self.swagger_types = {
            'directed': bool,
            'multigraph': bool,
            'elements': GraphElements
        }

        self.attribute_map = {
            'directed': 'directed',
            'multigraph': 'multigraph',
            'elements': 'elements'
        }
        self._directed = directed
        self._multigraph = multigraph
        self._elements = elements

    @classmethod
    def from_dict(cls, dikt) -> 'Graph':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Graph of this Graph.  # noqa: E501
        :rtype: Graph
        """
        return util.deserialize_model(dikt, cls)

    @property
    def directed(self) -> bool:
        """Gets the directed of this Graph.


        :return: The directed of this Graph.
        :rtype: bool
        """
        return self._directed

    @directed.setter
    def directed(self, directed: bool):
        """Sets the directed of this Graph.


        :param directed: The directed of this Graph.
        :type directed: bool
        """

        self._directed = directed

    @property
    def multigraph(self) -> bool:
        """Gets the multigraph of this Graph.


        :return: The multigraph of this Graph.
        :rtype: bool
        """
        return self._multigraph

    @multigraph.setter
    def multigraph(self, multigraph: bool):
        """Sets the multigraph of this Graph.


        :param multigraph: The multigraph of this Graph.
        :type multigraph: bool
        """

        self._multigraph = multigraph

    @property
    def elements(self) -> GraphElements:
        """Gets the elements of this Graph.


        :return: The elements of this Graph.
        :rtype: GraphElements
        """
        return self._elements

    @elements.setter
    def elements(self, elements: GraphElements):
        """Sets the elements of this Graph.


        :param elements: The elements of this Graph.
        :type elements: GraphElements
        """
        if elements is None:
            raise ValueError("Invalid value for `elements`, must not be `None`")  # noqa: E501

        self._elements = elements
