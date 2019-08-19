"""
Chapter 4 - Problem 4.5 - Validate BST
Problem:
Implement a function to check if a binary tree is a binary search tree.

Solution:
1. Clarify the question:
Repeat the question: We are given a binary tree, and we need to check whether it is a binary search tree.

Clarify assumptions: - Definition of a BST:
                       The left subtree of a node contains only nodes with keys less than the node's key.
                       The right subtree of a node contains only nodes with keys greater than the node's key.

2. Inputs and outputs:
So we're taking in a binary tree and returning True or False for whether it is a BST.

3. Test and edge cases:
edge: We can also take in an empty tree or None object.
test: We can also take in regular inputs like this:

    4
   / \
  1   6
    /  \
   5    7
and we will return True.

    4
   / \
  1   3
    /  \
   5    7
and we will return False as 3 is in the right subtree of its parent node 4.

4. Brainstorm solution:
Because of BST condition, we could do In-Order Traversal of the given tree and store the result in a temp array.
Then check if the temp array is sorted in ascending order, if it is, then the tree is BST.
Time-Complexity of the solution would be O(N) for in-order traversal and O(N) to check if the list is sorted.
Space-complexity would be O(N) since you need to hold the traversed list in memory. We can avoid the use of Auxiliary
Array. While doing In-Order traversal, we can keep track of previously visited node. If the value of the currently
visited node is less than the previous value, then tree is not BST.

We could also look at each node only once. We could traverse down the tree keeping track of the narrowing min and max
allowed values as it goes, looking at each node only once. The initial values for min and max should be INT_MIN and
INT_MAX — they narrow from there.

Note that we need to prepare a Class for the node which will hold and initialize the data for the node.

5. Runtime analysis:
Time complexity: O(N) as we traverse all the nodes in the tree once.
Space complexity: O(1) as we do not use any additional memory.

6. Code
"""
import sys
import unittest

class TreeNode:
    def __init__(self, value):
        """
        Creates a node for a tree.

        Attributes:
            value: A value of the node
            left: A reference to left child node
            right: A reference to right child node
        """
        self.value = value
        self.left = None
        self.right = None


"""
NOTE: Maximum integer value is sys.maxsize and minimum integer value is one less number on negative side i.e. -(sys.maxsize - 1)
"""

def is_bst(node, min_value=-(sys.maxsize - 1), max_value=sys.maxsize):
    """
    Checks if the tree/sub-tree rooted by the specified node is BST

    Args:
        node: An instance of the class TreeNode
        min_value: Lower bound for node values in the tree
        max_value: Upper bound for node values in the tree

    Returns:
        A boolean for whether it is a BST.
    """

    if node is None:
        return True

    # False if this node violates min/max constraint
    if node.value < min_value or node.value > max_value:
        return False

    # check recursively for every node.
    # tightening the min or max constraint
    return is_bst(node.left, min_value, node.value-1) and is_bst(node.right, node.value+1, max_value)


class TestBst(unittest.TestCase):
    def test_none(self):
        self.assertTrue(is_bst(None))

    def test_left_skewed(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        self.assertTrue(is_bst(root))

    def test_right_skewed(self):
        root = TreeNode(4)
        root.left = TreeNode(1)
        root.right = TreeNode(6)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(7)
        self.assertTrue(is_bst(root))

    def test_non_bst(self):
        root = TreeNode(4)
        root.left = TreeNode(5)
        root.right = TreeNode(6)
        self.assertFalse(is_bst(root))


if __name__ == '__main__':
    unittest.main()