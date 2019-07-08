"""
Chapter 2 - Problem 2.1 - Remove Dups
Problem:
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?

Solution:
1. Clarify the question:
Repeat the question: We are given a linked list which is unsorted. And we need to remove duplicate nodes from it.
Clarify assumptions: - Does the linked list have loops? (We will assume no.)
                     - Is it a singly or doubly linked list? (We will assume singly.).

2. Inputs and outputs:
So we're taking in a linked list and returning a linked list with duplicates removed.

3. Test and edge cases:
edge: we can also take in an empty linked list or None object as an input.
test: 4->3->10->4->2->9->2 should convert to 4->3->10->2->9.

4. Brainstorm solution:
If the linked list has zero or only one node, or none object, we can just return the linked list as there would be no
duplicates for sure.
We can iterate through the list and keep track of the values we see in each node in a hashtable or in python a dictionary
or set. When we encounter a value that we have seen before (meaning we need to do a lookup in hashtable, which takes
constant time), we remove it by rearranging the references of the previous node. The time complexity would be O(N) in
always case as we need to iterate through the list. The space complexity would be O(N) in worse case to store N keys in the set.
In the best case where we have only 1 unique element, it would be O(1).

If not using a buffer, we can compare all values with all other values by running two loops. The time complexity would
become O(N2) in always case. The space complexity would be constant in always case.

5. Runtime analysis:
time complexity: O(N) in always case for solution 1, O(N2) in always case for solution 2.
space complexity: - O(N) for solution 1
                  - O(1) for solution 2.

6. Code
"""
import unittest
from linkedlist import Node


# Solution
def remove_duplicates1(head):

    if not isinstance(head, Node):
        return -1

    if head.next is None:
        return head

    if head is not None:
        current = head
        seen = {current.value: 1}
        while current.next is not None:
            if current.next.value in seen:
                # remove node:
                current.next = current.next.next
            else:
                seen[current.next.value] = 1
                current = current.next

    return head


# Solution 2
def remove_duplicates2(head):
    if not isinstance(head, Node):
        return -1

    if head.next is None:
        return head

    current = head
    while current is not None:
        runner = current
        while runner.next is not None:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    return head


# Test and debug
class Test(unittest.TestCase):
    def setUp(self):
        self.head = Node(1)
        self.head.next = Node(3)
        self.head.next.next = Node(1)

        self.head2 = Node(0)

        self.head3 = None


    def test_remove_duplicates1(self):
        remove_duplicates1(self.head)
        self.assertEqual(self.head.value, 1)
        self.assertEqual(self.head.next.value, 3)
        self.assertEqual(self.head.next.next, None)

        remove_duplicates1(self.head2)
        self.assertEqual(self.head2.value, 0)
        self.assertEqual(self.head2.next, None)

        remove_duplicates1(self.head3)
        self.assertEqual(self.head3, None)

    def test_remove_duplicates2(self):
        remove_duplicates2(self.head)
        self.assertEqual(self.head.value, 1)
        self.assertEqual(self.head.next.value, 3)
        self.assertEqual(self.head.next.next, None)

        remove_duplicates2(self.head2)
        self.assertEqual(self.head2.value, 0)
        self.assertEqual(self.head2.next, None)

        remove_duplicates2(self.head3)
        self.assertEqual(self.head3, None)


if __name__ == "__main__":
    unittest.main()




