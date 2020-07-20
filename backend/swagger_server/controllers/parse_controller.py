import connexion
import six
import networkx as nx

from swagger_server.models.graph import Graph
from swagger_server import util


def upload_file(file, additional_metadata):
    """Parse graph from attached file
    :param file:
    :type file: strstr
    :param additional_metadata:
    :type additional_metadata: str
    :rtype: Graph
    """
    G = nx.read_edgelist(file)
    graph_data = nx.readwrite.json_graph.cytoscape_data(G)
    return graph_data
