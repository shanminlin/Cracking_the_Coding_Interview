"""
Chapter 2 - Problem 2.4 - Partition
Problem:
Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes
greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements
less than x. The partition element x can appear anywhere in the "right partition"; it does not need to appear
between the left and right partitions.

Solution:
1. Clarify the question:
Repeat the question: So we are given a linked list and a value x, and we need to shift the elements in the linked list
such that the elements less that x come before the elements greater or equal to x.
Clarify assumptions: - Does the linked list have loops? (We will assume no.)
                     - Is it a singly or doubly linked list? (We will assume singly.).

2. Inputs and outputs:
input: 3 -> 1 -> 4 -> 6 -> 7  [x = 4]
output: 3 -> 1 -> 6 -> 7 -> 4

3. Test and edge cases:
edge: So we can also take in an empty head as an input.
test: We can also have regular input like this: 3 -> 1 -> 4 -> 6 -> 7  [x = 4]

4. Brainstorm solution:
We can create two linked lists named less and greater. Iterate through the original list, if the current node has value
less than x, add it to the less list. Otherwise, add it to the greater list. After we reach the end of the original list,
combine the less and greater lists.
Note that we can start the less and greater lists with heads pointing to None. But there would require additional steps as
we will be adding to list by changing the next reference and None object has no next references. So we will use dummy
node as the head.

5. Runtime analysis:
Time complexity: O(N) as we need to iterate through the linked list.
Space complexity: O(1). We are just rearranging references and not creating any new nodes except the two dummy head nodes,
therefore we don't need additional spaces except the two dummy nodes.

6. Code
"""
import unittest
from linkedlist import Node


def partition(head, x):
    """Partitions a linked list around value x.

        Args:
          head: A node instance, which is the head node of a linked list.
          x: An integer.

        Returns:
          A linked list with elements shifted around value x.
        """
    less = less_head = Node(0)
    greater = greater_head = Node(0)

    while head is not None:
        # assign it to the less list
        if head.value < x:
            less.next = head
            less = less.next
        else:
            # assign it to the greater list.
            greater.next = head
            greater = greater.next

        head = head.next

    # combine before and after lists to form a single list
    # we need to skip the dummy head node in the greater list.
    less.next = greater_head.next

    return less_head.next


# 7. Test and debug
class Test(unittest.TestCase):
    def test_partition(self):
        head = Node(5)
        head.next = Node(3)
        head.next.next = Node(1)
        head.next.next.next = Node(2)
        head.next.next.next.next = Node(4)

        head2 = None

        result_head = partition(head, 3)
        self.assertEqual(result_head.value, 1)
        self.assertEqual(result_head.next.value, 2)
        self.assertEqual(result_head.next.next.value, 5)
        self.assertEqual(result_head.next.next.next.value, 3)
        self.assertEqual(result_head.next.next.next.next.value, 4)

        result_head2 = partition(head2, 3)
        self.assertEqual(result_head2, None)


if __name__ == "__main__":
    unittest.main()