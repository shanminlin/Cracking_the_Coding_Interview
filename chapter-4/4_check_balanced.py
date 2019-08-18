"""
Chapter 4 - Problem 4.4 - Check Balanced
Problem:
Implement a function to check if a binary tree is balanced. For the purpose of this question,
a balanced tree is defined to be a tree such that the heights of the two subtrees of any node
never differ by more than one.

Solution:
1. Clarify the question:
Repeat the question: We are a binary tree, for example:

    4
   / \
  1   2
    /  \
   6    7

And we need to check whether it is balanced.

Clarify assumptions: - definition of balanced: the heights of the left and right subtree are the same or differ by just 1.

2. Inputs and outputs:
So we're taking in a binary tree and returning True or False for whether it is a balanced tree.

3. Test and edge cases:
edge: We can also take in an empty tree or None object.
test: We can also take in regular inputs like this:

       1
      / \
     2   3
    / \
   4   5
  / \
 6   7

And we would return False.

4. Brainstorm solution:
If the input tree is empty or None, we would immediately return True. For other inputs like [4, 1, 2, null, null, 6, 7],
we can compute the height of left and right subtree for each node, and check the difference. If it is greater than 1,
return false. The time complexity would be O(N^2) in worse-case when the tree is skewed as we need to traverses the tree
to compute the heights for every node.

To improve time complexity, we could traverse all the way down to leaf nodes and then go up. While going up, compute the
left and right subtree height. If the difference is more than 1, return False. Otherwise, the height would be max(left_height, right_height) +1.
Here we don't compute the height of the subtrees, but store the height at each level and when we go one level up, we add one to it.
So Time complexity would be O(N). The space complexity would be O(h) where h is the height of the tree.


5. Runtime analysis:
Time complexity: - O(NlogN) in average-case, O(N^2) for worst-case when the tree is skewed for solution 1 as get_height
                   is O(N) and traversing binary tree is O(logN);
                 - O(N) for solution 2
Space complexity: - O(1) for solution 1
                  - O(h) in worst-case for solution 2, where h is the height of the tree.

6. Code
"""
import unittest


class TreeNode:
    """Creates a tree node"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Solution 1
def get_height(root):
    """Finds the height of a binary tree"""

    # base condition when reaching leaf node
    if root is None:
        return 0

    return max(get_height(root.left), get_height(root.right)) + 1


def is_balanced1(root):
    """Checks whether a binary tree is height-balanced."""

    # Base condition when reaching leaf node
    if root is None:
        return True

    # for left and right subtree height
    left_height = get_height(root.left)
    right_height = get_height(root.right)

    if abs(left_height - right_height) > 1:
        return False

    return is_balanced1(root.left) and is_balanced1(root.right)


# Solution 2
def is_balanced2(root):
    """Checks whether a binary tree is height-balanced."""

    # Base condition when reaching leaf node
    if root is None:
        return 0, True # return both height and whether it is balanced.

    # check whether left subtree is balanced and also get its height.
    left_height, left_is_balanced = is_balanced2(root.left)

    if not left_is_balanced:
        return 0, False

    # check whether right subtree is balanced and also get its height.
    right_height, right_is_balanced = is_balanced2(root.right)

    if not right_is_balanced:
        return 0, False

    # check if current node is unbalanced
    if abs(left_height - right_height) > 1:
        return 0, False

    # if we reach here, it means everything is balanced, return height
    return max(left_height, right_height) + 1, True


# 7. Test and debug
class Test(unittest.TestCase):
    def setUp(self):
        """
              1
           /   \
          2     3
        / \    /
       4   5  6

        """
        self.root = TreeNode(1)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(3)
        self.root.left.left = TreeNode(4)
        self.root.left.right = TreeNode(5)
        self.root.right.left = TreeNode(6)

    def test_is_balanced1(self):
        self.assertTrue(is_balanced1(self.root))

    def test_is_balanced2(self):
        self.assertEqual(is_balanced2(self.root), (3, True))


if __name__ == "__main__":
    unittest.main()
