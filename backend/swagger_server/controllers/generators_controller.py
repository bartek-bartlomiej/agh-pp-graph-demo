import connexion
import six
import networkx as nx

from swagger_server.models.generator import Generator
from swagger_server.models.graph import Graph
from swagger_server import util

N = 5
STEP = 1

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
def diamond_graph(P):
    return nx.diamond_graph()
def frucht_graph(P):
    return nx.frucht_graph()
def icosahedral_graph(P):
    return nx.icosahedral_graph()
def krackhardt_kite_graph(P):
    return nx.krackhardt_kite_graph()

# Social networks
def karate_club_graph(P):
    return nx.karate_club_graph()
def davis_southern_women_graph(P):
    return nx.davis_southern_women_graph()
def florentine_families_graph(P):
    return nx.florentine_families_graph()
def les_miserables_graph(P):
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

def default_n_bounded(min, max):
    PN = {"name": "n", "value": N}
    PN.update({"min": min})
    PN.update({"max": max})
    PN.update({"step": STEP})
    return [PN]

generators_parameters = {
    "binomial_tree": default_n_bounded(1, 10),
    "complete_graph": default_n_bounded(1, 100),
    "circular_ladder_graph": default_n_bounded(5, 70),
    "ladder_graph": default_n_bounded(2, 80),
    "dorogovtsev_goltsev_mendes_graph": default_n_bounded(1, 6),
    "star_graph": default_n_bounded(1, 200),

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

    entity = Generator.from_dict(connexion.request.get_json())
    generator_name = entity.name
    params = entity.parameters

    if not generator_name in generators_map.keys():
        return 'Invalid generator name'
    if not params:
        params = []

    P = parse_parameters(params)
    G = generators_map.get(generator_name)(P)
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
