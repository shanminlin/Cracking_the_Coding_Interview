"""
Chapter 2 - Problem 2.7 - Intersection
Problem:
Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the
intersection is defined based on reference, not value. That is, if the kth node of the first linked list is the exact
same node (by reference) as the jth node of the second linked list, then they are intersecting.

Solution:
1. Clarify the question:
Repeat the question: We are given two singly linked lists, and we need to check if the two lists intersect and we need to
return the intersecting node.
Clarify assumptions: - Does the linked list have loops? (We will assume no.)

2. Inputs and outputs:
So we're taking in the head nodes from two linked lists and returning the intersecting node if they intersect. Otherwise
return None.

3. Test and edge cases:
edge: So we can also take in empty nodes as inputs.
test: We can have regular inputs like this:


1 -> 2 -> 3 -> 4 ->
                    9 -> 10 -> 11
5 -> 6 -> 7 -> 8 ->


Here we have two linked lists 1 -> 2 -> 3 -> 4 -> 9 -> 10 -> 11 and 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11.
The intersecting node is node 9.

4. Brainstorm solution:
We can store the nodes in linked list 1 in a hash table. And then iterate through linked list 2, if a node seen in list 1,
meaning that is the 1st intersecting node, and we can return that node. The time complexity would be O(M+N) where M, N
are the number of nodes in the two lists, as we need to iterate through the two lists. The space complexity would be
O(N) where N is the number of nodes in the first linked list.
To reduce space complexity, we can maintain two pointers in the lists and move the pointers simultaneously until they
are at the same nodes (intersect). Note that if the two lists have different length, we have to advance the pointer
for the longer lists until the two lists have the same length. The time complexity would be O(M+N) as we need to calculate
the length of each list and also iterate through the two lists until they intersect. The space complexity would be O(1) as
we are not creating any new nodes.

5. Runtime analysis:
Time complexity: O(M+N) where M and N are number of nodes in the two lists.
Space complexity: O(N) for solution 1 as we need to use a hashtable.
                  O(1) for solution 2.

6. Code
"""
import unittest
from linkedlist import Node


def intersection1(head1, head2):
    list1_nodes = {}
    current1 = head1
    while current1 is not None:
        list1_nodes[current1] = True
        current1 = current1.next

    current2 = head2
    while current2 is not None:
        if current2 in list1_nodes:
            return current2
        current2 = current2.next
    return None


def intersection2(head1, head2):
    if head1 is None or head2 is None:
        return None

    current1 = head1
    current2 = head2
    length1 = 0
    length2 = 0
    while current1 is not None:
        length1 += 1
        current1 = current1.next
    while current2 is not None:
        length2 += 1
        current2 = current2.next

    # advance current pointer for longer list
    current1 = head1
    current2 = head2
    if length1 > length2:
        for i in range(length1-length2):
            current1 = current1.next
    elif length1 < length2:
        for i in range(length2-length1):
            current2 = current2.next

    while current1 is not current2:
        current1 = current1.next
        current2 = current2.next
    return current1


# 7. Test and debug
class Test(unittest.TestCase):
    def setUp(self):
        self.head1 = Node(1)
        self.head1.next = Node(3)
        self.head1.next.next = Node(2)

        self.head2 = Node(4)
        self.head2.next = Node(5)
        self.head2.next.next = Node(6)

        self.intersect_node1 = Node(5)
        self.intersect_node2 = Node(6)
        self.head3 = Node(1)
        self.head3.next = Node(2)
        self.head3.next.next = self.intersect_node1
        self.head3.next.next.next = self.intersect_node2
        self.head4 = Node(3)
        self.head4.next = Node(4)
        self.head4.next.next = self.intersect_node1
        self.head4.next.next.next = self.intersect_node2

        self.head5 = None
        self.head6 = Node(1)

        self.head7 = Node(1)
        self.head7.next = Node(2)
        self.head7.next.next = Node(3)
        self.head8 = Node(2)
        self.head8.next = Node(3)

    def test_intersection1(self):
        self.assertIsNone(intersection1(self.head1, self.head2))
        self.assertEqual(intersection1(self.head3, self.head4), self.intersect_node1)
        self.assertIsNone(intersection1(self.head5, self.head6))
        self.assertIsNone(intersection1(self.head7, self.head8))

    def test_intersection2(self):
        self.assertIsNone(intersection2(self.head1, self.head2))
        self.assertEqual(intersection2(self.head3, self.head4), self.intersect_node1)
        self.assertIsNone(intersection2(self.head5, self.head6))
        self.assertIsNone(intersection2(self.head7, self.head8))


if __name__ == "__main__":
    unittest.main()
