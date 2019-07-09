"""
Chapter 2 - Problem 2.3 - Delete Middle Node
Problem:
Implement an algorithm to delete a node in the middle (i.e. any node but the first and last node, not necessarily the
exact middle) of a singly linked list, given only access to that node.

Solution:
1. Clarify the question:
Repeat the question: So we are given a node in the middle of a singly linked list, and we need to remove that node from
the list.
Clarify assumptions: - Does the linked list have loops? (We will assume no.)

2. Inputs and outputs:
For example, we're taking in the node 3 from the linked list 2 -> 1 -> 3 -> 6, and returning nothing, but the list
becomes 2 -> 1 -> 6.

3. Test and edge cases:
edge: We can also take in an empty node as an input.
test: We can also have regular input like this: the node b from the linked list a -> b -> c -> d -> e

4. Brainstorm solution:
To delete a node, we will need to change the next reference of the previous node. But as we don't have access to the
previous node, we cannot use this method.
We could also copy the content of the next node to the node that need to be deleted.
In the above case, node b now will contain the value of c and node c will be invalid. Any previous references to node c
will become invalid,
If the input linked list is NULL, then it should remain NULL.

Note that we can't just use node_b = node_b.next because this only changes the object that the local variable
node_b refers to; the linked list is not modified.

5. Runtime analysis:
Time complexity: O(1).
Space complexity: O(1).

6. Code
"""
import unittest
from linkedlist import Node


def delete_middle_node(middle_node):
    if middle_node is not None:
        middle_node.value = middle_node.next.value
        middle_node.next = middle_node.next.next


# 7. Test and debug
class Test(unittest.TestCase):
    def test_delete_middle_node(self):
        head = Node(2)
        head.next = Node(1)
        head.next.next = Node(3)
        head.next.next.next = Node(6)
        head2 = None

        delete_middle_node(head.next.next)
        self.assertEqual(head.value, 2)
        self.assertEqual(head.next.value, 1)
        self.assertEqual(head.next.next.value, 6)

        delete_middle_node(head2)
        self.assertEqual(head2, None)


if __name__ == "__main__":
    unittest.main()