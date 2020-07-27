import connexion
import six
import networkx as nx

from swagger_server.models.arrangment_info import ArrangmentInfo
from swagger_server.models.layout import Layout
from swagger_server.models.node_position import NodePosition
from swagger_server import util

SCALE = 1000
WEIGHT = None

# Graph layouts
def circular_layout(G, P):
    return nx.circular_layout(G, scale=P["scale"])
def kamada_kawai_layout(G, P):
    return nx.kamada_kawai_layout(G, scale=P["scale"], weight=P["weight"])
def planar_layout(G, P):
    return nx.planar_layout(G, scale=P["scale"])
def random_layout(G, P):
    return nx.random_layout(G, scale=P["scale"])
def shell_layout(G, P):
    return nx.shell_layout(G, scale=P["scale"])
def spring_layout(G, P):
    return nx.spring_layout(G, scale=P["scale"], weight=P["weight"], k=P["k"], \
        iterations=P["iterations"], threshold=P["threshold"])
def spectral_layout(G, P):
    return nx.spectral_layout(G, scale=P["scale"], weight=P["weight"])
def spiral_layout(G, P):
    return nx.spiral_layout(G, scale=P["scale"], weight=P["weight"], \
        resolution=P["resolution"], equidistant=P["equidistant"])

layouts_map = {
    "circular_layout": circular_layout,
    "kamada_kawai_layout": kamada_kawai_layout,
    "planar_layout": planar_layout,
    "random_layout": random_layout,
    "shell_layout": shell_layout,
    "spring_layout": spring_layout,
    "spectral_layout": spectral_layout,
    "spiral_layout": spiral_layout,
}

WEIGHT_PARAM = {
    "name": "weight",
    "value": WEIGHT
}

SCALE_PARAM = {
    "name": "scale",
    "value": SCALE
}

K_PARAM = {
    "name": "k"
    "value": None # float = 1 / sqrt(n)
}

ITER_PARAM = {
    "name": "iterations",
    "value": 50
}

THRESHOLD_PARAM = {
    "name": "threshold",
    "value": 0.0001
}

RESOLUTION_PARAM = {
    "name": "resolution",
    "value": 0.35
}

EQUIDISTANT_PARAM = {
    "name": "equidistant",
    "value": False
}

ALL_PARAMS = [SCALE_PARAM, WEIGHT_PARAM, K_PARAM, ITER_PARAM, \
    THRESHOLD_PARAM, RESOLUTION_PARAM, EQUIDISTANT_PARAM]

layouts_parameters = {
    "circular_layout": [SCALE_PARAM],
    "kamada_kawai_layout": [SCALE_PARAM, WEIGHT_PARAM],
    "planar_layout": [SCALE_PARAM],
    "random_layout": [SCALE_PARAM],
    "shell_layout": [SCALE_PARAM],
    "spring_layout": [SCALE_PARAM, WEIGHT_PARAM, K_PARAM, ITER_PARAM, THRESHOLD_PARAM],
    "spectral_layout": [SCALE_PARAM, WEIGHT_PARAM],
    "spiral_layout": [SCALE_PARAM, WEIGHT_PARAM, RESOLUTION_PARAM, EQUIDISTANT_PARAM],
}

def parse_parameters(params):
    P = {}
    for d in ALL_PARAMS:
        P.update({d.get("name"), d.get("value")})
    for p in params:
        P.update({p.name: p.value})
    return P

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
    params = entity.parameters

    if not layout_name in layouts_map.keys():
        return 'Invalid layout algorithm name'
    if not graph:
        return 'Graph data is missing'

    G = cyto_to_nx(graph)
    P = parse_parameters(params)
    # G = nx.readwrite.json_graph.cytoscape_graph(graph.to_dict())
    POS = layouts_map.get(layout_name)(G, P)

    NODES = []
    for k, v in POS.items():
        NODES.append({"id": str(k), "x": str(v[0]), "y": str(v[1])})
    return NODES


def get_algorithms():
    """Returns supported NetworkX layout algorithms
    :rtype: List[Layout]
    """
    AL = []
    for k, v in layouts_parameters.items():
        AL.append({"name": k, "parameters": v})
    return AL
