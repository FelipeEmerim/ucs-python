"""Package that contains the Node class."""


class Node:

    """
    Represents a node in a graph.

    Attributes:
        - node_name: The name of the node. Must be unique to avoid conflicts
        - connections: The nodes this node connects to. (neighbors)
        - path: The path used to get to this node. This is used by the algorithm
        - path_weight: The weight of the path used to get to this node. Filled by the algorithm

    """

    def __init__(self, node_name):
        """
        Build a node object

        :param node_name: The name of the node.
        """
        self.node_name = node_name
        self.connections = []
        self.path = tuple()
        self.path_weight = 0

    def add_connection(self, node, weight):
        """
        Add a new connection to this node.

        :param node: The node to connect to.
        :param weight: The weight of this connection

        :return: None
        """

        if node not in self.connections:
            self.connections.append((weight, node,))
