"""
Chapter 2 - Problem 2.5 - Sum Lists
Problem:
You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in
reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and
returns the sum as a linked list.
FOLLOW UP:
Suppose the digits are stored in forward order. Repeat the above problem.

Solution:
1. Clarify the question:
Repeat the question: We are given two singly linked list, representing two numbers in reverse order of magnitude, meaning
the first element in the linked list is the ones place of the number, the second element the tens place etc. and we need
to compute the sum of the two lists and store the value in a linked list in the same format.
Clarify assumptions: - Negative integers (We will assume no.)

2. Inputs and outputs:
So we're taking in the head node of two singly linked lists and returning the head node of a linked list which represents
their sum.

3. Test and edge cases:
edge: We can also take in an empty head as an input.
test: We can also have regular input like this: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is 617 + 295
      And output: 2 -> 1 -> 9. That is 912.

4. Brainstorm solution:
Think about how we sum two digits. We can iterate through both linked lists, get nodes of both lists and add the values
and carry (initially set to 0) one by one.  If the sum is greater than 10, carry would be equal to 1 and the new sum
would be the ones digit., which can be computed as sum % 10.

5. Runtime analysis:
Time complexity: O(M+N) where M and N are number of nodes in the two lists.
Space complexity: O(N) as we need additional space for the sum.

6. Code
"""
import unittest
from linkedlist import Node


def sum_lists(num1, num2):
    if num1 is None or num2 is None:
        return num1 or num2

    carry = 0

    # We use a dummy node as the head of the sum list.
    # We can also set the head as None.
    # But this needs more if-else checks as we move head through the list using head.next as None has no next parameter.
    head = new_head = Node(0)
    
    while num1 is not None or num2 is not None:
        # caution: don't forget to check for None
        if num1 is None:
            num1_value = 0
        else:
            num1_value = num1.value

        if num2 is None:
            num2_value = 0
        else:
            num2_value = num2.value

        num_sum = carry + num1_value + num2_value

        if num_sum >= 10:
            carry = 1
            num_sum = num_sum % 10
        else:
            carry = 0

        current = Node(num_sum)
        head.next = current

        head = head.next

        # caution: don't forget to check for None
        if num1 is not None:
            num1 = num1.next
        if num2 is not None:
            num2 = num2.next

    if carry > 0:
        current.next = Node(carry)

    return new_head.next


# 7. Test and debug
class Test(unittest.TestCase):
    def test_sum_lists(self):
        head1 = Node(5)
        head1.next = Node(8)
        head1.next.next = Node(7)

        head2 = Node(3)
        head2.next = Node(8)

        result_sum = sum_lists(head1, head2)
        self.assertEqual(result_sum.value, 8)
        self.assertEqual(result_sum.next.value, 6)
        self.assertEqual(result_sum.next.next.value, 8)

        head3 = None
        head4 = None
        result_sum2 = sum_lists(head3, head4)
        self.assertEqual(result_sum2, None)


if __name__ == "__main__":
    unittest.main()