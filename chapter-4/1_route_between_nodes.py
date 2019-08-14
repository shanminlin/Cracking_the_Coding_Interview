"""
Chapter 4 - Problem 4.1 - Route Between Nodes
Problem:
Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

Solution:
1. Clarify the question:
Repeat the question: We are a given directed graph for example:

A----->B----->C
 \     |
  \    |
   \   |
    \  v
     ->D----->E

And for given two nodes for example A and E, we need to check whether there is a node between them.

Clarify assumptions: - Is there a loop?
                       (Assume yes.)

2. Inputs and outputs:
So we're taking in two nodes in a directed graph and returning True or False for whether there is a route between them.

3. Test and edge cases:
edge: We can also take in an empty node or None object.
test: We can also take in regular inputs like this: node B and E in the above example, and we need to return True.

4. Brainstorm solution:
We can use either Breadth First Search (BFS) or Depth First Search (DFS) to find path between two nodes. So we can start
with one node, perform a BFS or DFS. If we see the other node in our search, return true. Otherwise return false.

5. Runtime analysis:
Time complexity: O(V+E) in worst-case as we need to traverse all vertices and edges. V denotes vertice and E denotes edges.
Space complexity: O(V+E) in worst-case

6. Code
"""
import unittest


class GraphNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, new_node):
        self.children.append(new_node)

    def remove_child(self, del_node):
        if del_node in self.children:
            self.children.remove(del_node)


class Graph:
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)


def check_route(start_node, end_node):
    """Checks whether there is a route between two nodes in a directed graph."""
    if not isinstance(start_node, GraphNode) or not isinstance(end_node, GraphNode):
        return None

    visited = []

    # Create a stack for DFS
    stack = [start_node]

    while stack:
        # pop a node from stack
        current_node = stack.pop()
        visited.append(current_node)

        # if this node is the end_node, return True
        if current_node.value == end_node.value:
            return True

        # else, continue with DFS
        for child in current_node.children:
            if child not in visited:
                stack.append(child)

    # if DFS is completed without encountering end_node, return False
    return False


# 7. Test and debug
class Test(unittest.TestCase):
    def test_check_route(self):
        # create a graph
        nodeA = GraphNode('A')
        nodeB = GraphNode('B')
        nodeC = GraphNode('C')
        nodeD = GraphNode('D')
        nodeE = GraphNode('E')

        graph1 = Graph([nodeA, nodeB, nodeC, nodeD, nodeE])
        graph1.add_edge(nodeA,nodeB)
        graph1.add_edge(nodeA,nodeD)
        graph1.add_edge(nodeB,nodeC)
        graph1.add_edge(nodeB,nodeD)
        graph1.add_edge(nodeD,nodeE)

        self.assertTrue(check_route(nodeA, nodeE))
        self.assertFalse(check_route(nodeC, nodeE))
        self.assertTrue(check_route(nodeA, nodeA))
        self.assertIsNone(check_route(nodeA, None))


if __name__ == "__main__":
    unittest.main()
