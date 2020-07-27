import connexion
import six
import networkx as nx

from swagger_server.models.generator import Generator
from swagger_server.models.graph import Graph
from swagger_server import util

N = 5
MIN = 0
MAX = 200

# Classic
def binomial_tree(P):
    return nx.binomial_tree(P["n"])
def complete_graph(P):
    return nx.complete_graph(P["n"])
def circular_ladder_graph(P):
    return nx.circular_ladder_graph(P["n"])
def ladder_graph(P):
    return nx.ladder_graph(P["n"])
def dorogovtsev_goltsev_mendes_graph(P):
    return nx.dorogovtsev_goltsev_mendes_graph(P["n"])
def star_graph(P):
    return nx.star_graph(P["n"])

# Small
def diamond_graph():
    return nx.diamond_graph()
def frucht_graph():
    return nx.frucht_graph()
def icosahedral_graph():
    return nx.icosahedral_graph()
def krackhardt_kite_graph():
    return nx.krackhardt_kite_graph()

# Social networks
def karate_club_graph():
    return nx.karate_club_graph()
def davis_southern_women_graph():
    return nx.davis_southern_women_graph()
def florentine_families_graph():
    return nx.florentine_families_graph()
def les_miserables_graph():
    return nx.les_miserables_graph()

generators_map = {
    "binomial_tree": binomial_tree,
    "complete_graph": complete_graph,
    "circular_ladder_graph": circular_ladder_graph,
    "ladder_graph": ladder_graph,
    "dorogovtsev_goltsev_mendes_graph": dorogovtsev_goltsev_mendes_graph,
    "star_graph": star_graph,

    "diamond_graph": diamond_graph,
    "frucht_graph": frucht_graph,
    "icosahedral_graph": icosahedral_graph,
    "krackhardt_kite_graph": krackhardt_kite_graph,

    "karate_club_graph": karate_club_graph,
    "davis_southern_women_graph": davis_southern_women_graph,
    "florentine_families_graph": florentine_families_graph,
    "les_miserables_graph": les_miserables_graph,
}

DEFAULT_PARAMS = [{
    "name": "n",
    "value": N,
    "min": MIN,
    "max": MAX
}]

generators_parameters = {
    "binomial_tree": DEFAULT_PARAMS,
    "complete_graph": DEFAULT_PARAMS,
    "circular_ladder_graph": DEFAULT_PARAMS,
    "ladder_graph": DEFAULT_PARAMS,
    "dorogovtsev_goltsev_mendes_graph": DEFAULT_PARAMS,
    "star_graph": DEFAULT_PARAMS,

    "diamond_graph": [],
    "frucht_graph": [],
    "icosahedral_graph": [],
    "krackhardt_kite_graph": [],

    "karate_club_graph": [],
    "davis_southern_women_graph": [],
    "florentine_families_graph": [],
    "les_miserables_graph": [],
}

def parse_parameters(params):
    P = {"n": N}
    for p in params:
        P.update({p.name: p.value})
    return P

def generate(body):
    """Generate certain graph
    :param body: Generator name (and its parameters)
    :type body: dict | bytes
    :rtype: Graph
    """
    if not connexion.request.is_json:
        return 'Request has to be in JSON format'

    body = Generator.from_dict(connexion.request.get_json())
    if not body.name in generators_map.keys():
        return 'Invalid generator name'

    P = parse_parameters(body.parameters)

    G = generators_map.get(body.name)(P)
    graph_data = nx.readwrite.json_graph.cytoscape_data(G)
    return graph_data

def get_generators():
    """Returns supported NetworkX generators
    :rtype: List[Generator]
    """
    GL = []
    for k, v in generators_parameters.items():
        GL.append({"name": k, "parameters": v})
    return GL
