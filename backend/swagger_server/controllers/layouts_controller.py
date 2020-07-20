import connexion
import six
import networkx as nx

from swagger_server.models.arrangment_info import ArrangmentInfo
from swagger_server.models.layout import Layout
from swagger_server.models.node_position import NodePosition
from swagger_server import util

# Graph layouts
def circular_layout(G):
    return nx.circular_layout(G)
def kamada_kawai_layout(G):
    return nx.kamada_kawai_layout(G)
def planar_layout(G):
    return nx.planar_layout(G)
def random_layout(G):
    return nx.random_layout(G)
def shell_layout(G):
    return nx.shell_layout(G)
def spring_layout(G):
    return nx.spring_layout(G)
def spectral_layout(G):
    return nx.spectral_layout(G)
def spiral_layout(G):
    return nx.spiral_layout(G)


layouts_dict = {
    "circular_layout": circular_layout,
    "kamada_kawai_layout": kamada_kawai_layout,
    "planar_layout": planar_layout,
    "random_layout": random_layout,
    "shell_layout": shell_layout,
    "spring_layout": spring_layout,
    "spectral_layout": spectral_layout,
    "spiral_layout": spiral_layout,
}

def arrange(body):
    """Arrange graph
    :param body: Graph to arrange and algorithm info
    :type body: dict | bytes
    :rtype: List[NodePosition]
    """
    if not connexion.request.is_json:
        return 'Request has to be in JSON format'

    body = ArrangmentInfo.from_dict(connexion.request.get_json())
    if not body.layout.name in layouts_dict.keys():
        return 'Invalid layout algorithm name'
    if not body.graph:
        return 'Graph data is missing'

    G = nx.readwrite.json_graph.cytoscape_graph(body.graph)
    P = layouts_dict.get(body.layout)(G)
    return P


def get_layouts():
    """Returns supported NetworkX layout algorithms
    :rtype: List[Layout]
    """
    layouts = []
    for k, v in layouts_dict.items():
        layouts.append({"name": k})
    return layouts
