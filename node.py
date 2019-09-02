"""Package that contains the Node class."""
from typing import List, Tuple


class Node:

    """
    Represents a node in a graph.

    Attributes:
        - node_name: The name of the node. Must be unique to avoid conflicts
        - connections: The nodes this node connects to. (neighbors)
        - path: The path used to get to this node. This is used by the algorithm
        - path_weight: The weight of the path used to get to this node. Filled by the algorithm
        - x_position: The x position in the plane, used by astar
        - y_position: The y position in the plane, used by astar

    """

    def __init__(self, node_name: str, x_position: int = 0, y_position: int = 0):
        """
        Build a node object

        :param node_name: The name of the node.
        """
        self.node_name: str = node_name
        self.connections: List[Tuple[int, Node]] = []
        self.path: Tuple[Node] = tuple()
        self.path_weight: int or float = 0
        self.x_position: int = x_position
        self.y_position: int = y_position

    def add_connection(self, node: 'Node', weight: float or int):
        """
        Add a new connection to this node.

        :param node: The node to connect to.
        :param weight: The weight of this connection

        :return: None
        """

        if node not in self.connections:
            self.connections.append((weight, node,))
