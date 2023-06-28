#!/usr/bin/python3
"""
Module: 100-singly_linked_list
Class Node that defines a node of a singly linked list.
Class SinglyLinkedList that defines a singly linked list.
"""


class Node:
    """A node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """
        Initialize a Node object with data and next_node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): The next node in the linked list.
                Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the node."""
        return self._data

    @data.setter
    def data(self, value):
        """
        Set the data of the node.

        Args:
            value (int): The data value to be set.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Retrieve the next node in the linked list."""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the linked list.

        Args:
            value (Node): The next node to be set.

        Raises:
            TypeError: If the value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """A singly linked list."""

    def __init__(self):
        """Initialize an empty SinglyLinkedList."""
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the list.

        The list is maintained in increasing order.

        Args:
            value (int): The value to be inserted.
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and value > current.next_node.data:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Return a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)
