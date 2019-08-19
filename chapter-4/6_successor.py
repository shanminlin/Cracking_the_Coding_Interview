"""
Chapter 4 - Problem 4.6 - Successor
Problem:
Write an algorithm to find the 'next' node (i.e., in-order successor) of a given node in a binary search tree.
You may assume that each node has a link to its parent.

Solution:
1. Clarify the question:
Repeat the question: We are given a node in a binary search tree, and we need to find its in-order successor. For a BST,
in-order successor of a node is the smallest value greater than the value of the node.

Clarify assumptions: - Definition of a BST:
                       The left subtree of a node contains only nodes with keys less than the node's key.
                       The right subtree of a node contains only nodes with keys greater than the node's key.

2. Inputs and outputs:
So we're taking in a node in a binary search tree and returning its in-order successor.

3. Test and edge cases:
edge: We can also take in an empty node/tree.
test: We can also take in regular inputs like this: node 6 in the following BST,

    4
   / \
  1   6
    /  \
   5    7
and we will return 7.

4. Brainstorm solution:
We can divide this in 3 cases:
If the input node is a parent: we find if it has a right node and traverse to the leftmost child of the right node.
In case the right node has no children then the right node is its inorder successor. If there is no right node we need
to move up the tree to find the inorder successor.
If the input node is a left child: the parent is the inorder successor.
If the input node is a right child: We traverse up the tree until we find a node whose left subtree has the input node.
If the node is the rightmost node, there is no inorder successor.

5. Runtime analysis:
Time complexity:
Space complexity:

6. Code
"""
import unittest


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self


def get_successor(node):
    """Finds in-order successor of a node in a BST."""
    if node is None:
        return None

    current = node.right
    # Loops down to find the leftmost leaf
    while current is not None:
        if current.left is None:
            break
        current = current.left
    return current

    # if no leftmost leaf, find the ancestor
    if current is None:
        while node is not None:
            if node.parent is None:
                return None
            if node.parent.left == node:
                return node.parent  # right ancestor
            node = node.parent
        return node


class TestSuccessor(unittest.TestCase):
    def test_none(self):
        self.assertIsNone(get_successor(None))

    def test_left_skewed(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        self.assertEqual(get_successor(root).value, 6)

    def test_right_skewed(self):
        root = TreeNode(4)
        root.left = TreeNode(1)
        root.right = TreeNode(6)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(7)
        self.assertTrue(get_successor(root.right).value, 7)


if __name__ == '__main__':
    unittest.main()
