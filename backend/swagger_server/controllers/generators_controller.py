import connexion
import six
import networkx as nx

from swagger_server.models.generator import Generator  # noqa: E501
from swagger_server.models.graph import Graph  # noqa: E501
from swagger_server import util


def generate(body):  # noqa: E501
    """Generate certain graph

     # noqa: E501

    :param body: Generator name (and its parameters)
    :type body: dict | bytes

    :rtype: Graph
    """
    # if connexion.request.is_json:
    #     body = Generator.from_dict(connexion.request.get_json())  # noqa: E501
    # return 'do some magic!'

    K_3_5 = nx.complete_bipartite_graph(3, 5)
    graph_data = nx.readwrite.json_graph.cytoscape_data(K_3_5)

    return graph_data


def get_generators():  # noqa: E501
    """Returns supported NetowrkX generators

     # noqa: E501


    :rtype: List[Generator]
    """
    return 'do some magic!'
