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

def cyto_to_nx(graph):

    name = 'name'
    id = 'id'
    value = 'value'
    source = 'source'
    target = 'target'
    key = 'key'

    multigraph = graph.multigraph
    directed = graph.directed

    if multigraph:
        G = nx.MultiGraph()
    else:
        G = nx.Graph()
    if directed:
        G = G.to_directed()
    G.graph = {}

    for d in graph.elements.nodes:
        node_data = dict.fromkeys([name, id, value])
        node = d.data.value
        if d.data.name:
            node_data[name] = d.data.name
        if d.data.id:
            node_data[id] = d.data.id

        G.add_node(node)
        G.nodes[node].update(node_data)

    for d in graph.elements.edges:
        edge_data = dict.fromkeys([source, target, key])
        sour = d.data.source
        targ = d.data.target
        if multigraph:
            key = d.data.key
            G.add_edge(sour, targ, key=key)
            G.edges[sour, targ, key].update(edge_data)
        else:
            G.add_edge(sour, targ)
            G.edges[sour, targ].update(edge_data)
    return G

def arrange(body):
    """Arrange graph
    :param body: Graph to arrange and algorithm info
    :type body: dict | bytes
    :rtype: List[NodePosition]
    """
    if not connexion.request.is_json:
        return 'Request has to be in JSON format'

    entity = ArrangmentInfo.from_dict(connexion.request.get_json())
    layout_name = entity.layout.name
    graph = entity.graph

    if not layout_name in layouts_dict.keys():
        return 'Invalid layout algorithm name'
    if not graph:
        return 'Graph data is missing'

    G = cyto_to_nx(graph)
    # G = nx.readwrite.json_graph.cytoscape_graph(graph.to_dict())
    P = layouts_dict.get(layout_name)(G)

    NP = []
    for k, v in P.items():
        NP.append({"id": str(k), "x": str(v[0]), "y": str(v[1])})
    return NP


def get_algorithms():
    """Returns supported NetworkX layout algorithms
    :rtype: List[Layout]
    """
    layouts = []
    for k, v in layouts_dict.items():
        layouts.append({"name": k})
    return layouts
