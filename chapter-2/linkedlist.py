import unittest
"""
The following code is to demonstrate an implementation of a linked list with methods to manage list nodes.
To answer the questions in Chapter 2, you just need the Node class.
"""



class Node:
    """Define node for singly linked list.

    Attributes:
        value: Anything, a number, a string, a boolean or an object that a node stores.
        next: A reference to the next node in the list.
    """

    def __init__(self, value, next=None):
        """Inits node with value and next."""
        self.value = value
        self.next = next

    def __str__(self):
        """Print a readable string presentation of the object"""
        return str(self.value)


class LinkedList:
    """Singly linked list with methods to manage list nodes.

        Attributes:
            head: A node
        """

    def __init__(self):
        """Inits linked list"""
        self.head = None

    def __iter__(self):
        """Make linked list iterable"""
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)

    def add_to_end(self, value):
        """Add a new value to the end of the list."""
        if not isinstance(value, Node):
            new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def add_to_beginning(self, value):
        """Add a new value to the beginning of the list."""
        if not isinstance(value, Node):
            new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node


class LinkedListTest(unittest.TestCase):
    def setUp(self):
        self.node1 = Node(1)
        self.node2 = Node(2)
        self.node3 = Node(3)

        self.my_list = LinkedList()
        self.my_list.head = self.node1
        self.node1.next = self.node2
        self.node2.next = self.node3

    def test_append(self):
        self.my_list.add_to_end(4)
        self.assertEqual(str(self.my_list), '1 -> 2 -> 3 -> 4')

    def test_push(self):
        self.my_list.add_to_beginning(0)
        self.assertEqual(str(self.my_list), '0 -> 1 -> 2 -> 3')


if __name__ == "__main__":
    unittest.main()