"""
Chapter 4 - Problem 4.2 - Minimal Tree
Problem:
Given a sorted (increasing order) array with unique integer elements, write an algorithm to create
a binary search tree with minimal height.

Solution:
1. Clarify the question:
Repeat the question: We are a given a sorted array, and we need to create a binary search tree with minimal height.
                     For example, we want to convert [1, 2, 3] to a BST as follows:
                                   2
                                 /  \
                                1    3


Clarify assumptions:

2. Inputs and outputs:
So we're taking in an array such as [1, 2, 3] as input, and returning a BST.
                     Input: [1, 2, 3]
                     Output: A Balanced BST

3. Test and edge cases:
edge: We can also take in an empty array or None object or negative integers.
test: We can also take in regular inputs like [1, 2, 3, 4] and we need to return a BST.

4. Brainstorm solution:
To create a tree with minimal height, we want to have a BST as balanced as possible, meaning the number of nodes in the
left subtree need to match the number of nodes in the right subtree as much as possible. So what we can do is to take the
middle value of the sorted array to create a root node, then split the array into left and right section. Repeat this process
for the left and right section.

5. Runtime analysis:
Time complexity: O(NlogN) in worst-case as the recursion takes O(logN) and slicing takes O(N).
Space complexity: O(logN) in average-case for the recursive stack.

6. Code
"""


class Node:
    """Creates binary tree node"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def sorted_array_to_bst(arr):
    if not arr:
        return None

    if len(arr) == 1:
        return Node(arr)

    # find middle position
    mid = len(arr) // 2

    # make middle element the root
    root = Node(arr[mid])

    # create left subtree containing values < root
    root.left = sorted_array_to_bst(arr[:mid])

    # create right subtree containing values > root
    root.right = sorted_array_to_bst(arr[mid+1:])

    return root


# 7. Test and debug
def preorder_traverse(node):
    """Prints pre-order traversal of a binary search tree"""
    if not node:
        return None

    print(node.value)
    preorder_traverse(node.left)
    preorder_traverse(node.right)


arr = [1, 2, 3, 4, 5]
root = sorted_array_to_bst(arr)

preorder_traverse(root)
# print out 3, 2, 1, 5, 4