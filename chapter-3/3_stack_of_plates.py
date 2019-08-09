"""
Chapter 3 - Problem 3.3 - Stack of Plates
Problem:
Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life,
we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure
SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack
once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically
to a single stack (that is, pop() should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popA(int index) which performs a pop operation on a specific sub-stack.

Solution:
1. Clarify the question:
Repeat the question: We need to implement a SetOfStack class that consists of several stacks with maximum capacity. When
one stack exceeds maximum capacity, any new element will enter the next stack.
Clarify assumptions: - What if all stacks are full and we try to add more elements?
                       (A warning or an error message is thrown.)
                     - What if the stack is empty and we try to remove elements from this empty stack?
                       (A warning or an error message is thrown.)

2. Inputs and outputs:

3. Test and edge cases:

4. Brainstorm solution:
We can imagine the SetOfStack as one stack separating into several sub-stacks, so push and pop operations are performed on
the last sub-stack. We can implement the SetOfStack as a list of multiple lists.

- push:
When we push a new element, if the last sub-stack has capacity, we will push to the last sub-stack. Otherwise, we will append
the new element as a new list.

- pop:
We will pop from the last stack. Note that if after popping, the last stack becomes empty, we have to pop one more time
to remove the empty stack.

- pop_at:
We will assume no 'rolling over' behavior: after popping an element from stack 1, remove the first element from stack
2 to stack 1, etc.


5. Runtime analysis:
Time complexity: O(1) for push, pop and pop_at operations.
Space complexity: O(1) for push, pop and pop_at operations.

6. Code
"""
import unittest


class SetOfStack:
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError('Capacity must be larger than one.')
        else:
            self.capacity = capacity
        self.stacks = []

    def push(self, item):
        if self.stacks and len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item]) # append the item as a new list.

    def pop(self):
        if not self.stacks:
            raise AssertionError('Empty stack.')

        item = self.stacks[-1].pop()

        if len(self.stacks[-1]) == 0:
            self.stacks.pop()

        return item

    def pop_at(self, stack_number):
        # invalid input
        if stack_number < 1:
            raise ValueError('Stack number must be a positive integer.')

        stack_index = stack_number - 1
        # empty stack
        if len(self.stacks) < stack_number:
            raise AssertionError('Empty stack.')

        item = self.stacks[stack_index].pop()

        if len(self.stacks[-1]) == 0:
            self.stacks.pop()

        return item


class Test(unittest.TestCase):
    def test_set_of_stack(self):
        stack = SetOfStack(2)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        self.assertEqual(stack.pop(), 5)
        self.assertRaises(AssertionError, lambda: stack.pop_at(3))
        self.assertEqual(stack.pop_at(2), 4)
        self.assertEqual(stack.pop_at(2), 3)
        self.assertEqual(stack.pop_at(1), 2)
        self.assertEqual(stack.pop_at(1), 1)
        self.assertRaises(AssertionError, lambda: stack.pop())


if __name__ == "__main__":
    unittest.main()
