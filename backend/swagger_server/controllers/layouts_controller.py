import connexion
import six

from swagger_server.models.arrangment_info import ArrangmentInfo  # noqa: E501
from swagger_server.models.layout import Layout  # noqa: E501
from swagger_server.models.node_position import NodePosition  # noqa: E501
from swagger_server import util


def arrange(body):  # noqa: E501
    """Arrange graph

     # noqa: E501

    :param body: Graph to arrange and algorithm info
    :type body: dict | bytes

    :rtype: List[NodePosition]
    """
    if connexion.request.is_json:
        body = ArrangmentInfo.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_layouts():  # noqa: E501
    """Returns supported NetowrkX layout algorithms

     # noqa: E501


    :rtype: List[Layout]
    """
    return 'do some magic!'
