import connexion
import six
import networkx as nx

from swagger_server.models.generator import Generator
from swagger_server.models.graph import Graph
from swagger_server import util

N = 5
# Classic
def binomial_tree():
    return nx.binomial_tree(N)
def complete_graph():
    return nx.complete_graph(N)
def ladder_graph():
    return nx.ladder_graph(N)
def star_graph():
    return nx.star_graph(N)
def wheel_graph():
    return nx.wheel_graph(N)

# Small
def bull_graph():
    return nx.bull_graph()
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

generators_dict = {
    "binomial_tree": binomial_tree,
    "complete_graph": complete_graph,
    "ladder_graph": ladder_graph,
    "star_graph": star_graph,
    "wheel_graph": wheel_graph,

    "bull_graph": bull_graph,
    "diamond_graph": diamond_graph,
    "frucht_graph": frucht_graph,
    "icosahedral_graph": icosahedral_graph,
    "krackhardt_kite_graph": krackhardt_kite_graph,

    "karate_club_graph": karate_club_graph,
    "davis_southern_women_graph": davis_southern_women_graph,
    "florentine_families_graph": florentine_families_graph,
    "les_miserables_graph": les_miserables_graph,
}

def generate(body):
    """Generate certain graph
    :param body: Generator name (and its parameters)
    :type body: dict | bytes
    :rtype: Graph
    """
    if not connexion.request.is_json:
        return 'Request has to be in JSON format'

    body = Generator.from_dict(connexion.request.get_json())
    if not body.name in generators_dict.keys():
        return 'Invalid generator name'

    G = generators_dict.get(body.name)()
    graph_data = nx.readwrite.json_graph.cytoscape_data(G)
    return graph_data

def get_generators():
    """Returns supported NetowrkX generators
    :rtype: List[Generator]
    """
    generators = []
    for k, v in generators_dict.items():
        generators.append({"name": k})
    return generators
