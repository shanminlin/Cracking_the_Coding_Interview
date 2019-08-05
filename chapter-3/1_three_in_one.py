"""
Chapter 3 - Problem 3.1 - Three in One
Problem:
Describe how you could use a single array to implement three stacks.

Solution:
1. Clarify the question:
Repeat the question: We are given the array data structure, and we need to implement 3 stacks using a single array.
Clarify assumptions: - What functions must be supported by the stacks? (push/pop/size operations)
                     - What if the array is full and we try to add more elements?
                       (An error message is thrown when there is no space left in the stack which you want to add elements
                       into.)
                     - What if the stack is empty and we try to remove elements from any stack?
                       (An error message is thrown.)

2. Inputs and outputs:
So we're taking in the element and stack number that the element is going into.

3. Test and edge cases:
edge: We can also take in an empty element or None object as an input.
test: We can also have regular input like this: 4->3->10->4->2->9->2 should convert to 4->3->10->2->9.

4. Brainstorm solution:
Implementing two stacks is easy. First stack grows from start to end while second one grows from end to start.
Overflow for any of them will not happen unless there really is no space left in the array.

For three stacks, we need an auxiliary array to maintain the parent for each node and variables to store the current top of each
stack.

Divide the array in slots of size n/3: A simple way to implement k stacks is to divide the array in k slots of size n/k each,
and fix the slots for different stacks, i.e., use arr[0] to arr[n/k-1] for first stack, and arr[n/k] to arr[2n/k-1] for stack2
where arr[] is the array to be used to implement two stacks and size of array be n.

The problem with this method is inefficient use of array space. A stack push operation may result in stack overflow even
if there is space available in arr[]. For example, say the k is 2 and array size (n) is 6 and we push 3 elements to first
and do not push anything to second second stack. When we push 4th element to first, there will be overflow even if we have
space for 3 more elements in array.

You can start one of the stacks from one end of the array. You can start the other stack from the other end of the array.
You can put the third stack in the middle. When, one of the side stacks need space, you need to shift the middle stack.

To improve space efficiency,

5. Runtime analysis:
time complexity: O(N) in always case for solution 1, O(N2) in always case for solution 2.
space complexity: - O(N) for solution 1
                  - O(1) for solution 2.

6. Code
"""
import unittest


class ThreeStacks:

    def __init__(self, capacity):
        self.capacity = capacity  # Total size of array holding all three stacks.

        # Array which holds 'k' stacks.
        self.arr = [0] * self.capacity

        # All stacks are empty to begin with
        # (-1 denotes stack is empty).
        self.top = [-1] * 3

        # to keep track of stack size for is_empty, is_full methods
        self.sizes = [0] * 3

        # Top of the free stack.
        self.free = 0

        # Points to the next element in either
        # 1. One of the 'k' stacks or,
        # 2. The 'free' stack.
        self.next = [i + 1 for i in range(self.capacity)]
        self.next[self.capacity - 1] = -1

    # Check whether given stack is empty.
    def is_empty(self, stack_number):
        return self.top[stack_number] == -1

    # Check whether there is space left for
    # pushing new elements or not.
    def is_full(self):
        return self.free == -1

    # Push item onto given stack number
    def push(self, item, stack_number):
        if self.is_full():
            print("Stack Overflow")
            return

        # Get the first free position
        # to insert at.
        insert_at = self.free

        # Adjust the free position.
        self.free = self.next[self.free]

        # Insert the item at the free position we obtained above.
        self.arr[insert_at] = item

        # Adjust next to point to the old top of stack element.
        self.next[insert_at] = self.top[stack_number]

        # Set the new top of the stack.
        self.top[stack_number] = insert_at

    # Pop item from given stack number
    def pop(self, stack_number):
        if self.is_empty(stack_number):
            return None

        # Get the item at the top of the stack.
        top_of_stack = self.top[stack_number]

        # Set new top of stack.
        self.top[stack_number] = self.next[self.top[stack_number]]

        # Push the old top_of_stack to
        # the 'free' stack.
        self.next[top_of_stack] = self.free
        self.free = top_of_stack

        return self.arr[top_of_stack]


class Test(unittest.TestCase):
    def test_three_stacks(self):
        three_stacks = ThreeStacks(10)
        three_stacks.push(1, 0)
        three_stacks.push(2, 0)
        three_stacks.push(3, 0)
        three_stacks.push(1, 1)

        self.assertEqual(three_stacks.pop(0), 3)
        self.assertEqual(three_stacks.pop(1), 1)
        self.assertEqual(three_stacks.pop(1), None)
        self.assertEqual(three_stacks.pop(2), None)

        three_stacks.push(1, 2)
        three_stacks.push(2, 2)
        self.assertEqual(three_stacks.pop(2), 2)
        self.assertEqual(three_stacks.pop(2), 1)
        self.assertEqual(three_stacks.pop(2), None)


if __name__ == "__main__":
    unittest.main()
