"""
Chapter 4 - Problem 4.8 - First Common Ancestor
Problem:
Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree.
Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.

Solution:
1. Clarify the question:
Repeat the question: We are given two nodes in a binary tree, and we need to find the lowest common ancestor in the tree.
For example, for a binary tree    4
                                /  \
                               1    6
                             /  \  /  \
                            2   5  3  7

For two nodes 2 and 7, the first common ancestor would be the 4.

Clarify assumptions: - All of the nodes' values will be unique? (Assume yes.)
                     - Do we assume the two given nodes are different? (Yes.)
                     - Do we need to validate the input nodes exist in the tree? (No.)

2. Inputs and outputs:
So we're taking in two nodes in a binary tree and returning their first common ancestor.

3. Test and edge cases:
edge: We can also take in an empty node/tree.
test: We can also take in regular inputs like the above example.

4. Brainstorm solution:
We could traverse the tree starting from root. If either input node matches the root, the root is the lowest common
ancestor. Otherwise, we do recursion for left and right subtree. The node which has one input node present in its left subtree
and the other input node present in right subtree is the lowest common ancestor. If both input nodes are in the left subtree,
the left subtree has the lowest common ancestor. Otherwise the right subtree has the lowest common ancestor.

5. Runtime analysis:
Time complexity: O(N) in worst case where N is the number of nodes in a binary tree. This happens when the binary tree is skewed.
Space complexity: O(N) due space utilized by the recursion stack when the binary tree is skewed.

6. Code
"""
import unittest


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def lowest_common_ancestor(root, node1, node2):
    """Finds the lowest common ancestor of two nodes in a binary tree.

    Args:
        root: An instance of TreeNode
        node1: An instance of TreeNode
        node2: An instance of TreeNode

    Returns:
        An instance of TreeNode
    """
    # Base Case
    if root is None:
        return None

    if root == node1 or root == node2:
        return root

    left = right = None
    if root.left:
        left = lowest_common_ancestor(root.left, node1, node2)
    if root.right:
        right = lowest_common_ancestor(root.right, node1, node2)

    if left and right:
        return root
    else:
        return left or right

class TestAncestor(unittest.TestCase):
    def test_none(self):
        self.assertIsNone(lowest_common_ancestor(None, None, None))

    def test_left_skewed(self):
        """
                                  4
                                /  \
                               5    6
                             /  \
                            1   3


        """
        root = TreeNode(4)
        root.left = TreeNode(5)
        root.right = TreeNode(6)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        self.assertEqual(lowest_common_ancestor(root, root.left.left, root.left.right).value, 5)
        self.assertEqual(lowest_common_ancestor(root, root, root.left.right).value, 4)


if __name__ == '__main__':
    unittest.main()