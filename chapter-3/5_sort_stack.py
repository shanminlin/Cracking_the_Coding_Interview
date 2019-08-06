"""
Chapter 3 - Problem 3.5 - Sort Stack
Problem:
Write a program to sort a stack such that the smallest items are on the top.
You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as array).
The stack supports the following operations: push, pop, peek and isEmpty.

Solution:
1. Clarify the question:
Repeat the question: We are given a stack like [2, 3, 1, 5, 4], and we need to sort the stack in a descending order to
                     return [5, 4, 3, 2, 1].
                     The restriction is we cannot use additional data structures except an additional temporary stack.

Clarify assumptions: - Are we looking for stack as a last-in-first-out data structure? (Yes)
                     - What are the items that the stack is going to take as inputs? (numbers)
                     - Do we have duplicate numbers in the input? (Assume no.)
                     - Do we have gaps in the stack? (Assume no.)

2. Inputs and outputs:
So we're taking in a stack and returning a sorted stack with the smallest item on top.

3. Test and edge cases:
edge: We can also take in an empty stack or None object.
test: We can also take in regular inputs like this: [2, 3, 1, 5, 4] and we need to return [5, 4, 3, 2, 1].

4. Brainstorm solution:
Sorting a stack would not be time efficient compared to an array as arrays allow random-access.
With 2 stacks, one stack would be used to store sorted element. We can iterate until the original stack is empty. In each
iteration, pop an element from the original stack and store it a variable current_top. While the top element in the second
stack is larger than current_top, push current_top to the second stack. If the top element of the second stack is smaller
than current_top, pop the second stack and push it to the original stack. Repeat the process until the stack is sorted.

Example:
Original stack
+----+----+----+
| 5  | 1  | 6  |
+----+----+----+

pop 6 it off from original stack and current_top = 6. Push 6 to temporary stack:
Original stack                           Temporary stack
+----+----+                              +----+
| 5  | 1  |                              | 6  |
+----+----+                              +----+

current_top = 1 and pop it off. Since 6 > 1, push 1 to temporary stack:
Original stack                           Temporary stack
+----+                                   +----+----+
| 5  |                                   | 6  | 1  |
+----+                                   +----+----+

current_top = 5 and pop it off. Since 1 < 5, pop 1 from second stack and push it to original stack:
Original stack                           Temporary stack
+----+                                   +----+
| 1  |                                   | 6  |
+----+                                   +----+

since 6 > 5, push 5 to temporary stack
Original stack                           Temporary stack
+----+                                   +----+----+
| 1  |                                   | 6  | 5  |
+----+                                   +----+----+

current_top = 1. Since 5 > 1, push 1 to temporary stack:
                                         Temporary stack
                                         +----+----+----+
                                         | 6  | 5  | 1  |
                                         +----+----+----+


5. Runtime analysis:
Time complexity: O(N^2) in worst-case when the original stack is already sorted. The top element of the original stack
would need to be moved O(N) times. Therefore for all elements, the time complexity would be approx O(N^2) times.

Space complexity: O(N) as we need an additional stack

6. Code
"""
import unittest


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def __str__(self):
        return str(self.stack)


def sort_stack(stack):
    if stack is None or stack.is_empty():
        return None

    tmp_stack = Stack()
    while not stack.is_empty():
        current_top = stack.peek()
        stack.pop()

        while not tmp_stack.is_empty() and tmp_stack.peek() < current_top:
            stack.push(tmp_stack.peek())
            tmp_stack.pop()

        tmp_stack.push(current_top)

    return tmp_stack


class Test(unittest.TestCase):
    def test_sort_stack(self):
        self.assertEqual(sort_stack(Stack()), None)
        self.assertEqual(sort_stack(None), None)
        stack = Stack()
        stack.push(2)
        stack.push(3)
        stack.push(5)
        stack.push(1)
        stack.push(6)
        stack.push(4)
        self.assertEqual(str(stack), "[2, 3, 5, 1, 6, 4]")
        self.assertEqual(str(sort_stack(stack)), "[6, 5, 4, 3, 2, 1]")


if __name__ == "__main__":
    unittest.main()
