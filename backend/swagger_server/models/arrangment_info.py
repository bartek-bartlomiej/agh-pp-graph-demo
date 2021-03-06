# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.graph import Graph  # noqa: F401,E501
from swagger_server.models.layout import Layout  # noqa: F401,E501
from swagger_server import util


class ArrangmentInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, graph: Graph=None, layout: Layout=None):  # noqa: E501
        """ArrangmentInfo - a model defined in Swagger

        :param graph: The graph of this ArrangmentInfo.  # noqa: E501
        :type graph: Graph
        :param layout: The layout of this ArrangmentInfo.  # noqa: E501
        :type layout: Layout
        """
        self.swagger_types = {
            'graph': Graph,
            'layout': Layout
        }

        self.attribute_map = {
            'graph': 'graph',
            'layout': 'layout'
        }
        self._graph = graph
        self._layout = layout

    @classmethod
    def from_dict(cls, dikt) -> 'ArrangmentInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ArrangmentInfo of this ArrangmentInfo.  # noqa: E501
        :rtype: ArrangmentInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def graph(self) -> Graph:
        """Gets the graph of this ArrangmentInfo.


        :return: The graph of this ArrangmentInfo.
        :rtype: Graph
        """
        return self._graph

    @graph.setter
    def graph(self, graph: Graph):
        """Sets the graph of this ArrangmentInfo.


        :param graph: The graph of this ArrangmentInfo.
        :type graph: Graph
        """

        self._graph = graph

    @property
    def layout(self) -> Layout:
        """Gets the layout of this ArrangmentInfo.


        :return: The layout of this ArrangmentInfo.
        :rtype: Layout
        """
        return self._layout

    @layout.setter
    def layout(self, layout: Layout):
        """Sets the layout of this ArrangmentInfo.


        :param layout: The layout of this ArrangmentInfo.
        :type layout: Layout
        """

        self._layout = layout
