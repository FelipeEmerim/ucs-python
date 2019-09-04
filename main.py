"""Ucs search client."""
from astar import Astar
from ucs import Ucs
from node import Node


def print_result_info(result: tuple):
    print('Best possible path')

    print(' > '.join([e.node_name for e in result]))

    print('Path weight {}'.format(result[-1].path_weight))
    print('--------------------------------------------')


if __name__ == '__main__':

    node1 = Node('Node 1', x_position=10, y_position=10)

    # Astar should visit this node since it is real close to the goal
    # It should be visited before node three because node three is far from the goal
    node2 = Node('Node 2', x_position=99, y_position=99)
    node3 = Node('Node 3', x_position=30, y_position=30)
    node4 = Node('Node 4', x_position=20, y_position=10)

    node5 = Node('Node 5', x_position=40, y_position=40)
    node6 = Node('Node 6', x_position=100, y_position=100)
    node7 = Node('Node 7', x_position=90, y_position=90)
    node8 = Node('Node 8', x_position=120, y_position=120)

    # create connections
    node1.add_connection(node2, 7)
    node1.add_connection(node3, 2)

    node2.add_connection(node4, 5)

    node3.add_connection(node5, 3)

    node4.add_connection(node6, 1)

    node5.add_connection(node7, 3)
    node5.add_connection(node8, 4)

    node7.add_connection(node6, 3)

    node8.add_connection(node7, 1)

    # do search
    ucs = Ucs()

    print_result_info(ucs.run(start=node1, goal=node6))

    Node.reset_nodes()

    astar = Astar(heuristic_factor=0.05, heuristic=Astar.MANHATTAN_DISTANCE)

    print_result_info(astar.run(start=node1, goal=node6))
