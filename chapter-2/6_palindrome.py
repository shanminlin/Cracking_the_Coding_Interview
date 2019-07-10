"""
Chapter 2 - Problem 2.6 - Palindrome
Problem:
Implement a function to check if a linked list is a palindrome.

Solution:
1. Clarify the question:
Repeat the question: So we are given a linked list, and we need to check whether it is a palindrome.
Clarify assumptions: - Does the linked list have loops? (We will assume no.)
                     - Is it a singly or doubly linked list? (We will assume singly.).

2. Inputs and outputs:
So we're taking in the head node of a singly linked list and returning True or False for whether the linked list is a
palindrome.

3. Test and edge cases:
edge: We can also take in an empty node as an input.
test: We can also have regular input like this: a -> b -> c -> b -> a

4. Brainstorm solution:
As a palindrome reads the same forward and backward, we can make use of the concept of a stack (last in first out).
We can iterate through the linked list and push every node to a stack. As the first value popped from the stack would be the value from the last
node of the linked list (last in first out), we can pop each value from the stack one by one and compare that value
to each node from the linked list. If they match, return True. The time complexity would be O(N) as we need to iterate
through the list twice. The space complexity would be O(N) as we need additional space to store the stack.

We can reduce the space complexity by reversing half of the linked list and compare that to the other half. We first get
to the middle of the linked list, and reverse the 2nd half of the linked list. Then check if the 1st half and 2nd half
match. If so, return True. The time complexity would be O(N) as we need to iterate through the linked list twice (once for
computing length, we also need to iterate through half of the list twice). The space complexity would be O(1).

5. Runtime analysis:
Time complexity: O(N) as we need to iterate through the list at least once
Space complexity: O(N) for solution 1 due to additional stack; O(1) for solution 2.

6. Code
"""
import unittest
from linkedlist import Node

# Solution 1
def is_palindrome1(head):
    if head is None:
        return -1

    if head.next is None:
        return True

    current = head
    new_stack = []

    while current:
        new_stack.append(current.value)
        current = current.next

    current = head
    while current:
        data = new_stack.pop()
        if current.value != data:
            return False
        current = current.next

    return True


# Solution 2
def is_palindrome2(head):
    if head is None:
        return -1

    if head.next is None:
        return True

    # compute length
    length = 0
    current = head
    while current is not None:
        length += 1
        current = current.next

    # reverse first half of the linked list
    mid_length = length // 2
    reverse_first_half = Node(head.value)
    current = head
    for _ in range(mid_length-1):
        current = current.next
        node = Node(current.value, reverse_first_half)
        reverse_first_half = node

    # caution: don't forget to check None before current.next
    if current.next is not None:
        current = current.next  # move current node from 1st half to 2nd half
        if length % 2 != 0:  # one more step for odd numbered list
            current = current.next

    # compare reversed 1st half and 2nd half
    current2 = reverse_first_half
    while current2 is not None:
        if current2.value != current.value:
            return False
        current2 = current2.next
        current = current.next

    return True


# 7. Test and debug
class Test(unittest.TestCase):
    def setUp(self):
        self.head1 = Node(1)
        self.head2 = Node(1)
        self.head2.next = Node(2)
        self.head2.next.next = Node(5)
        self.head2.next.next.next = Node(2)
        self.head2.next.next.next.next = Node(1)
        self.head3 = Node(1)
        self.head3.next = Node(2)
        self.head4 = None

    def test_palindrome1(self):
        self.assertTrue(is_palindrome1(self.head1))
        self.assertTrue(is_palindrome1(self.head2))
        self.assertFalse(is_palindrome1(self.head3))
        self.assertEqual(is_palindrome1(self.head4), -1)

    def test_palindrome2(self):
        self.assertTrue(is_palindrome2(self.head1))
        self.assertTrue(is_palindrome2(self.head2))
        self.assertFalse(is_palindrome2(self.head3))
        self.assertEqual(is_palindrome2(self.head4), -1)


if __name__ == "__main__":
    unittest.main()
