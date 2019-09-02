"""Package that contains the Ucs class."""

from queue import PriorityQueue

from node import Node


class Ucs:

    """
    Class that contains logic related to the ucs algorithm.

    Note that this is a didatic implementation and is not good in performance.
    """

    def perform_ucs(self, start: Node, goal: Node):
        """
        Given a start and goal node, tries to find the best path.

        :param start: The start node
        :param goal: The goal node
        :return: A tuple of nodes containing the path
        """

        path = self._search(start, goal)

        return path

    def _search(self, start: Node, goal: Node) -> list:
        """
        Using a priority queue to find the best possible path given a start and goal node.

        :param start: The start node
        :param goal: The goal node

        :return: A tuple containing all nodes involved in the path

        :raise ValueError in case no path is found.
        """

        queue = PriorityQueue()
        queue.put((0, start))

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
                self._add_to_queue(weight + c_weight, c_node, queue, node_path)

        raise ValueError('No paths found')

    @staticmethod
    def _add_to_queue(weight: int, node: Node, queue: PriorityQueue, path: list):
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

        for q_weight, q_node in queue.queue:
            if q_node.node_name == node.node_name:

                if q_weight <= weight:
                    return

                queue.queue.remove((q_weight, q_node))
                break

        node.path = path
        node.path_weight = weight
        queue.put((weight, node))
