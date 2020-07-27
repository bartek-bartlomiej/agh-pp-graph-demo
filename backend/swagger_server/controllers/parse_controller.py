import connexion
import six
import networkx as nx

from swagger_server.models.graph import Graph
from swagger_server import util

def upload_file(file, weighted=None):
    """Parse graph from attached file with edge list
    :param file:
    :type file: strstr
    :param weighted: Is graph weighted
    :type weighted: bool
    :rtype: Graph
    """
    if (weighted):
        G = nx.read_weighted_edgelist(file)
    else:
        G = nx.read_edgelist(file)
    graph_data = nx.readwrite.json_graph.cytoscape_data(G)
    return graph_data
