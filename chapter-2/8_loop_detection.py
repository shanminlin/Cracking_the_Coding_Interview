"""
Chapter 2 - Problem 2.8 - Loop Detection
Problem:
Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.
DEFINITION:
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node,
so as to make a loop in the linked list.

Solution:
1. Clarify the question:
Repeat the question: So we are given a linked list that contains loop, and we need to find the 1st node of the loop.
Clarify assumptions: - Is it a singly or doubly linked list? (We will assume singly.).

2. Inputs and outputs:
So we're taking in the head node of a circular linked list and returning the 1st node of the loop.

3. Test and edge cases:
edge: We can also take in an empty node as an input.
test: We can also have regular input like this:
        input: A -> B -> C -> D -> E -> C [the same C as earlier]
        output: C

4. Brainstorm solution:
We can iterate through each node one by one and store each node's memory address in a hash table. If we encounter a node
already seen in the hash table, this indicates the node at the beginning of the loop. If we have reached the end of the
linked list without seeing any node in the hash table, we can return None as there is no loop. The time complexity would
be O(N) as we need to iterate through the list. The space complexity would be O(N) as we need additional space to store
the hash table.

To reduce space complexity, we can use two pointers: slow and fast pointer. Move fast by 2 steps and slow by 1 step. If
there is a loop, both pointers will enter the loop at some time and at some distance apart. Then at each iteration, their
distance will be shortened by 1. It is like keeping the slow pointer stationary and moving the fast pointer by 1 step.
Eventually they will meet. (If we let the fast pointer move by 3 steps instead of 2 steps, it is like keeping the slow
pointer stationary and moving the faster pointer 2 steps each time. The fast pointer may miss the slow pointer and they
never meet!）

Now they have met somewhere in the loop. Let's denote the length from head of the list to the beginning of the loop be m,
from the beginning of the loop to the meeting points be k, from meeting point TO the beginning of the loop be n. The
length of the loop would be k+n, which can be computed by keeping fast pointer stationary at the meeting point and moving
slow pointer until it meet fast pointer again and count number of nodes. We can also compute k+m by keeping past pointer
at the meeting point and moving slow pointer to the head of the list, and move it until it reaches fast and count the number
of nodes. If you calculate k+n and k+m, you will see that they are actually equal. So m = n. So the distance from meeting
point to the beginning of the loop is actually equal to the distance from head of the list to the beginning of the list.
So we can keep fast pointer at the meeting point and slow pointer at head and move them by 1 step. When they meet, the node
is the beginning of the loop.

The time complexity would be O(N) as we need to iterate through the list at least once. The space complexity would be O(1)
as we don't create new nodes or use additional data structures.

5. Runtime analysis:
Time complexity: O(N) for both solutions
Space complexity: O(N) for solution 1 as we need additional space for the hash table
                  O(1) for solution 2

6. Code
"""
import unittest
from linkedlist import Node


def find_loop1(head):
    seen_nodes = {}
    current = head
    while current is not None:
        if current in seen_nodes:
            return current
        seen_nodes[current] = True
        current = current.next
    return None


def find_loop2(head):
    slow = head
    fast = head

    # first run for detecting whether loop exists
    # caution: need to check both fast and fast.next not None
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break

    # need to check both fast and fast next as the fast pointer may be at any of there two positions at the end.
    if fast is None or fast.next is None:
        return None

    # to illustrate m == n in the above explanation
    else:
        distance_to_head = 0
        slow = head
        while slow is not fast:
            distance_to_head += 1
            slow = slow.next

        loop_length = 1
        slow = slow.next
        while slow is not fast:
            loop_length += 1
            slow = slow.next

        assert loop_length == distance_to_head

    # second run for detecting the first node of the loop
    slow = head
    while fast is not slow:
        fast = fast.next
        slow = slow.next

    return fast


# 7. Test and debug
class Test(unittest.TestCase):
    def setUp(self):
        self.head1 = Node(1)
        self.head1.next = Node(3)
        self.head1.next.next = Node(6)
        self.head1.next.next.next = Node(5)

        self.loop_node = Node(3)
        self.head2 = Node(1)
        self.head2.next = self.loop_node
        self.head2.next.next = Node(6)
        self.head2.next.next.next = Node(5)
        self.head2.next.next.next.next = Node(4)
        self.head2.next.next.next.next.next = self.loop_node

        self.head3 = None

        self.head4 = Node(1)
        self.head4.next = None

    def test_find_loop1(self):
        self.assertIsNone(find_loop1(self.head1))
        self.assertEqual(find_loop1(self.head2), self.loop_node)
        self.assertIsNone(find_loop1(self.head3))
        self.assertIsNone(find_loop1(self.head4))

    def test_find_loop2(self):
        self.assertIsNone(find_loop2(self.head1))
        self.assertEqual(find_loop2(self.head2), self.loop_node)
        self.assertIsNone(find_loop2(self.head3))
        self.assertIsNone(find_loop2(self.head4))


if __name__ == "__main__":
    unittest.main()
