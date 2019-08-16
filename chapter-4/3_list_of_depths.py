"""
Chapter 4 - Problem 4.3 - List of Depths
Problem:
Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth
(e.g., if you have a tree with depth D, you'll have D linkd list).

Solution:
1. Clarify the question:
Repeat the question: We are a given a binary tree, and we need to connect all the adjacent nodes at the same depth using
linked list.
                     For example,
Input:
       A
      / \
     B   C

Output:
       linked list 1: A ->NULL
       linked list 2: B-->C-->NULL

Clarify assumptions:

2. Inputs and outputs:
So we're taking in a binary tree, and returning k linked lists if the height of tree is k.

3. Test and edge cases:
edge: We can also take in an empty tree or None object or negative integers.
test: We can also take in regular inputs like A,  and we need to return two linked lists.
                                             / \
                                            B   C

4. Brainstorm solution:
We can do a level-order traversal throughout the tree. For each level, create a linked list containing all the nodes at
that depth. Then extract all of the children for each node to create the next linked list at deeper level.

5. Runtime analysis:
Time complexity:
Space complexity:

6. Code
"""
import unittest
from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None, depth=None):
        self.value = value
        self.left = left
        self.right = right
        self.depth = depth


class LinkedlistNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value) + ',' + str(self.next)


def list_of_depths(tree_node):
    if not tree_node:
        return []

    linkedlists = []
    queue = deque()

    current_depth = -1
    current_tail = None
    tree_node.depth = 0

    while tree_node:
        if tree_node.depth == current_depth:
            current_tail.next = LinkedlistNode(tree_node.value)
            current_tail = current_tail.next
        else:
            current_depth = tree_node.depth
            current_tail = LinkedlistNode(tree_node.value)
            linkedlists.append(current_tail)

        for child in [tree_node.left, tree_node.right]:
            if child:
                child.depth = tree_node.depth + 1
                queue.append(child)
        tree_node = queue.popleft()
    return linkedlists


# 7. Test and debug

class Test(unittest.TestCase):
    def test_list_of_depths(self):
        node_h = TreeNode('H')
        node_g = TreeNode('G')
        node_f = TreeNode('F')
        node_e = TreeNode('E', node_g)
        node_d = TreeNode('D', node_h)
        node_c = TreeNode('C', None, node_f)
        node_b = TreeNode('B', node_d, node_e)
        node_a = TreeNode('A', node_b, node_c)
        lists = list_of_depths(node_a)
        self.assertEqual(str(lists[0]), "A,None")
        self.assertEqual(str(lists[1]), "B,C,None")
        self.assertEqual(str(lists[2]), "D,E,F,None")
        self.assertEqual(str(lists[3]), "H,G,None")
        self.assertEqual(len(lists), 4)


if __name__ == "__main__":
    unittest.main()