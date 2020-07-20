import connexion
import six

from swagger_server.models.graph import Graph  # noqa: E501
from swagger_server import util


def upload_file(file, additional_metadata):  # noqa: E501
    """parse graph from attached files

     # noqa: E501

    :param file: 
    :type file: strstr
    :param additional_metadata: 
    :type additional_metadata: str

    :rtype: Graph
    """
    return 'do some magic!'
