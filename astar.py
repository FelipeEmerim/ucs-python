from math import sqrt
from typing import Callable

from algorithm import Algorithm
from node import Node


class Astar(Algorithm):
    """
    Class that contains logic related to the astar algorithm.

    Note that this is a didatic implementation and is not good in performance.
    """

    MANHATTAN_DISTANCE: str = 'MANHATTAN'
    EUCLIDEAN_DISTANCE: str = 'EUCLIDEAN'

    def __init__(self, precision: float or int, heuristic: str = MANHATTAN_DISTANCE):
        self.precision: float or int = precision
        self.heuristic: str = heuristic

    def manhattan_distance(self, node: Node, goal: Node) -> float or int:
        """
        Implementation of the manhattan distance heuristic.

        :param node: The current node.
        :param goal: The goal node.

        :return: The weight calculated by the heuristic.
        """
        x_distance = abs(node.x_position - goal.x_position)
        y_distance = abs(node.y_position - goal.y_position)

        return self.precision*(x_distance + y_distance)

    def euclidean_distance(self, node: Node, goal: Node) -> float or int:
        """
        Implementation of the euclidean distance heuristic.

        :param node: The current node.
        :param goal: The goal node.

        :return: The weight calculated by the heuristic.
        """
        x_distance = abs(node.x_position - goal.x_position)
        y_distance = abs(node.y_position - goal.y_position)

        return self.precision*(sqrt(x_distance * x_distance + y_distance * y_distance))

    def get_weight_function(self) -> Callable[[Node, Node], float or int]:
        """
        Return the function that will calculate the heuristic weight.

        :return: The callable.
        """
        functions = {self.MANHATTAN_DISTANCE: self.manhattan_distance,
                     self.EUCLIDEAN_DISTANCE: self.euclidean_distance}

        return functions.get(self.heuristic, self.manhattan_distance)
