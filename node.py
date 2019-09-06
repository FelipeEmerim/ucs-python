"""Package that contains the Node class."""
import math
from functools import total_ordering
from typing import List, Tuple


@total_ordering
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
        - node_list: the list of nodes, would represent the graph itself

    """

    node_list: ['Node'] = []

    def __init__(self, node_name: str, x_position: int = 0, y_position: int = 0):
        """
        Build a node object

        :param node_name: The name of the node.
        """
        self.node_name: str = node_name
        self.connections: List[Tuple[int, Node]] = []
        self.path: Tuple[Node] = tuple()
        self.path_weight: int or float = math.inf
        self.x_position: int = x_position
        self.y_position: int = y_position
        self.node_list.append(self)

    def add_connection(self, node: 'Node', weight: float or int):
        """
        Add a new connection to this node.

        :param node: The node to connect to.
        :param weight: The weight of this connection

        :return: None
        """

        if node not in self.connections and node is not self:
            self.connections.append((weight, node,))

    @classmethod
    def reset_nodes(cls):
        """
        Clear node info used by the algorithms.

        Avoid keeping multiple separate lists by keeping properties in the object.

        :return: None
        """

        for node in cls.node_list:
            node.path_weight = math.inf
            node.path = tuple()

    @classmethod
    def clear_nodes(cls):
        """
        Remove all nodes from the node list.

        :return: None
        """
        cls.node_list = []

    def __eq__(self, other: 'Node') -> bool:
        """
        Implements equals operator, names are used in the comparison.

        :param other: Node instance

        :return: A boolean indicating the name comparison
        """
        if not isinstance(other, Node):
            return NotImplemented
        return self is other

    def __lt__(self, other: 'Node') -> bool:
        """
        Implements the less than operator using the attribute node_name.

        :param other: Node instance

        :return: A boolean indicating the name comparison
        """
        if not isinstance(other, Node):
            return NotImplemented
        return self.node_name < other.node_name
