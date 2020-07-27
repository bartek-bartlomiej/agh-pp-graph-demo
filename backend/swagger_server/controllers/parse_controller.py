import connexion
import six
import networkx as nx

from swagger_server.models.graph import Graph
from swagger_server import util


def upload_file(file):
    """Parse graph from attached files
    :param file:
    :type file: strstr
    :rtype: Graph
    """
    G = nx.read_edgelist(file)
    graph_data = nx.readwrite.json_graph.cytoscape_data(G)
    return graph_data
