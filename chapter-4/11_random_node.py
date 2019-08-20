"""
Chapter 4 - Problem 4.11 - Random Node
Problem:
You are implementing a binary tree class from scratch which, in addition to insert, find and delete, has
a method getRandomNode() which returns a random node from the tree. All nodes should be equally likely
to be chosen. Design and implement an algorithm for getRandomNode, and explain how you would implement
the rest of the methods.

Solution:
1. Clarify the question:
Repeat the question: We are given a binary tree, and we need to implement a get_random_node() method which returns a
random node. Nodes will be selected with equal probability.

Clarify assumptions: - Definition of a BST:
                       The left subtree of a node contains only nodes with keys less than the node's key.
                       The right subtree of a node contains only nodes with keys greater than the node's key.

2. Inputs and outputs:
So we're taking in a binary tree and returning a random node.

3. Test and edge cases:
edge: We can also take in an empty tree.
test: We can also take in regular inputs like this:

       1
     /   \
   2      3
  / \    / \
 4   5  6   7
and if we can get_random_node(root), we will get a random node e.g. 3.

4. Brainstorm solution and runtime analysis:
We could copy all values in the tree into an array using any of the tree traversal methods. For N nodes, we generate a
random number from 0 to N-1. Then use this number as an index in the array and return the value at that index. The time
complexity would be O(N) in always case as we need to traverse the tree. The space complexity would be O(N) in always case
as we need to copy all nodes in the tree to an array. The time complexity for get_random_node() is O(1). If nodes were
not deleted from the tree, this solution would be fine. However, if nodes are deleted or inserted from the tree,
modifying arrays requires O(N) time.

To eliminate the use of an extra array, we could use a counter as we traverse the tree. So for each node we visit, increment
the counter. If the counter's value equals the randomly chosen number, pick that node. So the space complexity would be O(1)
in always case. But the time complexity is still O(N) in worst-case.

To reduce the time complexity, we could store the count of children in every node. We generate a number smaller than or equal count of nodes.
We traverse the tree and go to the node at that index. we reach in O(h) time where h is height of tree.

5. Code
"""
from random import randint

class Node:
    def __init__(self, value):
        self.value = value
        self.children = 0
        self.left = None
        self.right = None

# This is used to fill children counts.
def count_children(root):
    if root is None:
        return 0

    return count_children(root.left) + count_children(root.right) + 1

# Inserts Children count for each node
def insert_children_count(root):
    if root is None:
        return

    root.children = count_children(root) – 1
    insert_children_count(root.left)
    insert_children_count(root.right)

# Returns number of children for root
def children(root):
    if root is None:
     return 0
    return root.children + 1

# Helper Function to return a random node
def random_node_util(root, count):
    if root is None:
        return 0

    if count == children(root.left):
        return root.value

    if count < children(root.left):
        return random_node_util(root.left, count)

    return random_node_util(root.right, count - children(root.left) - 1)

    # Returns Random node
def random_node(root):
    count = randint(0, root.children)
    return random_node_util(root, count)