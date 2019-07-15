"""
Chapter 3 - Problem 3.4 - Queue via Stacks
Problem:
Implement a MyQueue class which implements a queue using two stacks.

Solution:
1. Clarify the question:
Repeat the question: We are given a stack data structure, and we need to implement a queue using 2 instances of the stack
data structure and associated methods.
Clarify assumptions: - Are we looking for stack as a last-in-first-out data structure and queue as a last-in-last-out
                       data structure? As we can also have a queue as double-ended queue. (Yes)
                     - What operations do we need to implement for MyQueue? (enqueue, dequeue)
                     - What if we want to dequeue from an empty queue? (return None)
                     - What if we want to add an element to a queue that is already full? (we will assume queues and stacks
                       are not fixed-sized.)
                     - What are the elements that MyQueue is going to take as inputs? (numbers, strings etc.)
                     - What operations do the stack support? (push to back, pop from front. We can implement our own stacks
                       or using Python list that support these stack operations)

2. Inputs and outputs:
So we're implementing a queue class using a stack class.

3. Test and edge cases:
edge: we will assume no pop from empty queue.
test: If we push an array of integers [1, 2, 3, 4, 5] to a queue, and dequeue the queue until the queue is empty,
      the output will be [1, 2, 3, 4, 5].

4. Brainstorm solution:
The difference between a queue and a stack is that a stack is Last-in-first-out and a queue is Last-in-last out. So if
we push an array of integers [1, 2, 3, 4, 5, 6] to a stack and pop the elements until the stack is empty, the elements popped
out will be [6, 5, 4, 3, 2, 1], which is the reverse of the input order. For the same input order, if we dequeue the queue
until the queue is empty, the output will be [1, 2, 3, 4, 5, 6], which follows the same input order.

So when we push [1, 2, 3, 4, 5, 6] into a stack and pop every element off, we get [6, 5, 4, 3, 2, 1]. If we push that output
to a second stack and pop every element off the second stack, we will get [1, 2, 3, 4, 5, 6], which is exactly the output
we expect from a queue.

5. Runtime analysis:
Time complexity:
For enqueue, each element will be pushed to two stacks (two push operations), which would be O(1) in always-case.
For dequeue, as we will implement our stack as python list which is array based, the time complexity would be O(N)
in worst case when we call dequeue the first time (as we need to pop every element in the first stack to second stack).
But for the following dequeue operations, the time complexity would be O(1) as we only need to pop elements from the
second stack. So worse case is always followed by many O(1). So amortized O(1).

Space complexity: O(N)

6. Code
"""
import unittest


class MyQueue:
    def __init__(self):
        self.first_stack = []
        self.second_stack = []

    def dequeue(self):
        if not self.second_stack:
            while self.first_stack:
                pop_from_first = self.first_stack.pop()
                self.second_stack.append(pop_from_first)
        return self.second_stack.pop()

    def enqueue(self, value):
        self.first_stack.append(value)


# 7. Test and debug
class Test(unittest.TestCase):
    def test_myqueue(self):
        queue = MyQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.dequeue(), 1)
        queue.enqueue(3)
        queue.enqueue('a')
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 'a')


if __name__ == "__main__":
    unittest.main()

