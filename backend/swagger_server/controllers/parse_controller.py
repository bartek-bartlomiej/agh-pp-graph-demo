import connexion
import six
import networkx as nx

from swagger_server.models.graph import Graph
from swagger_server import util

def upload_file(body):
    """Parse graph from attached files
    :param body:
    :type body: dict | bytes
    :rtype: Graph
    """
    if not connexion.request.is_json:
        return 'Request has to be in JSON format'

    body = Object.from_dict(connexion.request.get_json())
    G = nx.read_edgelist(body)
    graph_data = nx.readwrite.json_graph.cytoscape_data(G)
    return graph_data
