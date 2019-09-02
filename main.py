"""Ucs search client."""

from ucs import Ucs
from node import Node

if __name__ == '__main__':

    # Create nodes
    node1 = Node('Node 1')
    node2 = Node('Node 2')
    node3 = Node('Node 3')
    node4 = Node('Node 4')
    node5 = Node('Node 5')
    node6 = Node('Node 6')
    node7 = Node('Node 7')
    node8 = Node('Node 8')

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

    result = ucs.perform_ucs(start=node1, goal=node6)

    # output
    string_path = []
    total_weight = 0

    print('Best possible path')

    print(' > '.join([e.node_name for e in result]))

    print('Path weight {}'.format(result[-1].path_weight))
