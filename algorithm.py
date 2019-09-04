from queue import PriorityQueue
from typing import Tuple, Callable

from node import Node


class Algorithm:

    """
    Class that contains logic related to the ucs algorithm.

    Note that this is a didatic implementation and is not good in performance.
    """

    def run(self, start: Node, goal: Node) -> tuple:
        """
        Given a start and goal node, tries to find the best path.

        :param start: The start node
        :param goal: The goal node
        :return: A tuple of nodes containing the path
        """

        path: Tuple[Node] = self._search(start, goal)

        return path

    def _search(self, start: Node, goal: Node) -> tuple:
        """
        Using a priority queue to find the best possible path given a start and goal node.

        :param start: The start node
        :param goal: The goal node

        :return: A tuple containing all nodes involved in the path

        :raise ValueError in case no path is found.
        """

        queue = PriorityQueue()
        start.path_weight = 0
        queue.put((0, start))

        calculate_heuristic = self.get_weight_function()

        while not queue.empty():
            weight, current_node = queue.get()
            print('Visiting node {}, weight {}'.format(current_node.node_name, weight))

            if current_node == goal:
                final_path = current_node.path
                final_path += (current_node,)
                return final_path

            node_path = current_node.path
            node_path += (current_node,)

            for c_weight, c_node in current_node.connections:

                weight_so_far = current_node.path_weight + c_weight
                estimated_weight = weight_so_far + calculate_heuristic(c_node, goal)

                self._add_to_queue(weight_so_far, estimated_weight, c_node, queue, node_path)

        raise ValueError('No paths found')

    @staticmethod
    def _add_to_queue(weight: int, estimated_weight: float or int, node: Node, queue: PriorityQueue, path: list):
        """
        Add a path to a node to the queue given a weight.

        If the node is not in the queue it is added straight forward.

        If the node is already in the queue it is only added in case it weight is less than
        the weight of the path already in the queue.

        :param weight: The weight of this path
        :param node: The end node of the path
        :param queue: The priority queue that contains all the paths
        :param path: The path to get to this node

        :return: None
        """

        # if node was already visited by a lesser cost, do not requeue it
        if node.path_weight <= weight:
            return

        for q_weight, q_node in queue.queue:
            if q_node.node_name == node.node_name:

                if q_weight <= weight:
                    return

                queue.queue.remove((q_weight, q_node))
                break

        node.path = path
        node.path_weight = weight
        queue.put((estimated_weight, node))

    def get_weight_function(self) -> Callable[[Node, Node], int or float]:
        """
        Must return the function that is responsible for calculating the weight of the path.

        The function must take two parameters, current_node and goal.

        :return: The function that will calculate the weight.
        """
        return lambda x, y: 0
