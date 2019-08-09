"""
Chapter 3 - Problem 3.2 - Stack Min
Problem:
How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element?
Push, pop and min should all operate in O(1) time.

Solution:
1. Clarify the question:
Repeat the question: We need to implement a stack with push, pop and min operations, all take O(1) time in worst case.
Clarify assumptions: - What if the stack is full and we try to add more elements?
                       (Assume no maximum capacity.)
                     - What if the stack is empty and we try to remove elements from this empty stack?
                       (A warning or an error message is thrown.)

2. Inputs and outputs:
So we're taking in a stack and returning minimum element.

3. Test and edge cases:
edge: We can also take in an empty stack or None object.
test: We can also take in regular inputs like this: [2, 3, 1, 5, 4] and we need to return 1.

4. Brainstorm solution:
We may use a member variable in a stack to keep track of the minimum element as we push elements into a stack. But this
could fail when we pop elements off and one of the elements is the minimum element.
So to address this, we could use two stacks: the actual stack to store the stack elements. The other stack to store the
same number of elements as the actual stack, but only the minimum of all elements lower in the stack.

Example:

Actual stack                           Minimum stack
+----+----+----+----+               +----+----+----+----+
| 5  | 1  | 6  | 2  |               | 5  | 1  | 1  | 1  |
+----+----+----+----+               +----+----+----+----+
                  |                                   |
                 top                                 top


After popping one element:
Actual stack                           Minimum stack
+----+----+----+                    +----+----+----+
| 5  | 1  | 6  |                    | 5  | 1  | 1  |
+----+----+----+                    +----+----+----+

To form the minimum stack, we need to modify the pop and push operations for a typical stack:
- min:
The current minimum is always the top element of the minimum stack.

- push:
When we push the very first element, we push to both stacks. Subsequently, when we push a new element to the actual stack,
push to the minimum stack either the new element or the current top (min) of the minimum stack, whichever is smaller.

- pop:
When we pop the actual stack, pop the minimum stack as well.


5. Runtime analysis:
Time complexity: O(1) in always-case as the top of the minimum stack is always the minimum element.
Space complexity: O(N) as we need an additional stack

6. Code
"""
import unittest


# solution 1
class MinStack1():
    def __init__(self):
        self.actual_stack = []
        self.min_stack = []

    def push(self, item):

        # push to minimum stack
        if len(self.actual_stack) == 0:
            self.min_stack.append(item)
        else:
            self.min_stack.append(min(self.min_stack[-1], item))

        # push to actual stack
        self.actual_stack.append(item)

    def pop(self):
        if self.is_empty():
            raise AssertionError('Empty stack')
        self.min_stack.pop()
        return self.actual_stack.pop()

    def get_min(self):
        if self.is_empty():
            raise AssertionError('Empty stack')
        return self.min_stack[-1]

    def is_empty(self):
        return len(self.actual_stack) == 0


# solution 2
class MinStack2:
    def __init__(self):
        self.stack = []

    def push(self, element):
        current_min = self.get_min()
        if current_min is None or element < current_min:
            current_min = element
        self.stack.append((element, current_min))

    def pop(self):
        if len(self.stack) == 0:
            return None
        self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1][0]

    def get_min(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1][1]


class Test(unittest.TestCase):
    def test_min_stack1(self):
        min_stack = MinStack1()
        with self.assertRaises(AssertionError):
            min_stack.get_min()
        min_stack.push(4)
        min_stack.push(3)
        self.assertEqual(min_stack.get_min(), 3)
        min_stack.push(6)
        min_stack.pop()
        min_stack.pop()
        self.assertEqual(min_stack.get_min(), 4)
        min_stack.pop()
        with self.assertRaises(AssertionError):
            min_stack.get_min()

    def test_min_stack2(self):
        min_stack = MinStack2()
        self.assertEqual(min_stack.get_min(), None)
        min_stack.push(4)
        min_stack.push(3)
        self.assertEqual(min_stack.get_min(), 3)
        min_stack.push(6)
        min_stack.pop()
        self.assertEqual(min_stack.peek(), 3)
        min_stack.pop()
        self.assertEqual(min_stack.get_min(), 4)
        min_stack.pop()
        self.assertEqual(min_stack.get_min(), None)


if __name__ == "__main__":
    unittest.main()