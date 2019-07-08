"""
Chapter 2 - Problem 2.2 - Return Kth to Last
Problem:
Implement an algorithm to find the kth to last element of a singly linked list.

Solution:
1. Clarify the question:
We are given a singly linkedlist. And we need to find the kth to last element. For example, we have a singly linked list
4->3->10->5->2. if k = 1, we would return 2, if k =2, we would return 5.
Clarify assumptions: - Does the linked list have loops? (We will assume no.)

2. Inputs and outputs:
So we're taking in the head node of a singly linked list and returning the kth last element.

3. Test and edge cases:
edge: So we can also take in an empty head or None object as an input.
test: We can also have regular input like this: the head of 4->3->10->5->2

4. Brainstorm solution:
As we are given the length from the end of the list, we could calculate the length from the  beginning of the list,
which is the length of the whole list - k + 1. So we could first iterate through the linked list
to find its length, and then iterate through the list by (length of the list - k + 1) steps to get the kth-to-last node.
The time complexity would be O(N) as we need to iterate through the list twice. The space complexity would be constant.

We could also iterate through the list once by using a queue with length k. Then add nodes unitl the end of the list to
the queue. As the list is longer than the queue. length - k nodes will be removed. We will be left of k nodes and the first
element in this queue with k nodes would be the kth-to-last node. The time complexity is stll O(N) but we only need to
iterate through the list once, but the space complexity would be O(N) as well as we need additonal space for the queue.

To further reduce the space complexity, we could use two points that are separated by k-1 nodes. When the faster pointer
gets to the end, the slower pointer would be at the kth node from the end. The time complexity would be O(N) and the
space complexity would be O(1).

5. Runtime analysis:
time complexity: O(N) in always case for solution 1, 2 and 3
space complexity: - O(N) for solution 2.
                  - O(1) for solution 1 and 3.


6. Code
"""
import unittest
from linkedlist import Node


# Solution 1
def kth_to_last_node1(head, k):
    """Return the kth-to-last node of a linked list.

    Args:
      head: A node instance, which is the head node of a linked list.
      k: An integer.

    Returns:
      The kth-to-last node.

    Raises:
      IndexError: if k is smaller than 1 or greater than the length of the list.
    """
    
    if k < 1:
        raise IndexError("Index out of range")

    current = head
    length = 0
    while current is not None:
        length += 1
        current = current.next

    if k > length:
        raise IndexError("Index out of range")

    kth_node = head
    for _ in range(length - k):
        kth_node = kth_node.next

    return kth_node


# Solution 2
from collections import deque


def kth_to_last_node2(head, k):
    """Return the kth-to-last node of a linked list.

    Args:
        head: A node instance, which is the head node of a linked list.
        k: An integer.

    Returns:
        The kth-to-last node.

    Raises:
        IndexError: if k is smaller than 1 or greater than the length of the list.
    """

    if k < 1:
        raise IndexError("Index out of range")

    queue = deque(maxlen=k)
    node = head
    while node is not None:
        queue.append(node)
        node = node.next

    if len(queue) != k:
        raise IndexError("Index out of range")

    return queue[0]


# Solution 3
def kth_to_last_node3(head, k):
    """Return the kth-to-last node of a linked list.

    Args:
        head: A node instance, which is the head node of a linked list.
        k: An integer.

    Returns:
        The kth-to-last node.

    Raises:
        IndexError: if k is smaller than 1 or greater than the length of the list.
    """

    if k < 1:
        raise IndexError("Index out of range")

    current = head
    runner = head

    for _ in range(k):
        runner = runner.next
        if runner is None:
            raise IndexError("Index out of range")


    while runner is not None:
        current = current.next
        runner = runner.next

    return current


# 7. Test and debug
class Test(unittest.TestCase):
    def setUp(self):
        self.head = Node(1)
        self.head.next = Node(3)
        self.head.next.next = Node(2)
        self.head.next.next.next = Node(5)

    def test_kth_to_last_node1(self):
        with self.assertRaises(IndexError):
            kth_to_last_node1(self.head, 0)
        self.assertEqual(kth_to_last_node1(self.head, 1).value, 5)
        self.assertEqual(kth_to_last_node1(self.head, 3).value, 3)
        with self.assertRaises(IndexError):
            kth_to_last_node1(self.head, 8)

    def test_kth_to_last_node2(self):
        with self.assertRaises(IndexError):
            kth_to_last_node2(self.head, 0)
        self.assertEqual(kth_to_last_node2(self.head, 1).value, 5)
        self.assertEqual(kth_to_last_node2(self.head, 3).value, 3)
        with self.assertRaises(IndexError):
            kth_to_last_node2(self.head, 8)

    def test_kth_to_last_node3(self):
        with self.assertRaises(IndexError):
            kth_to_last_node3(self.head, 0)
        self.assertEqual(kth_to_last_node3(self.head, 1).value, 5)
        self.assertEqual(kth_to_last_node3(self.head, 3).value, 3)
        with self.assertRaises(IndexError):
            kth_to_last_node3(self.head, 8)


if __name__ == "__main__":
    unittest.main()
