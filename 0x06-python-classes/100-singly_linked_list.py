#!/usr/bin/python3
"""This is a module that defines a node of a singly linked list
"""


class Node:
    """Node class defines the node of a singly linked list by private
    instance attribute data and private instance attribute next_node

    Attribute:
            __data - an integer
            __next_node - a node object
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """This property retrieves data

        Returns: int
        """
        return self.__data

    @data.setter
    def data(self, value):
        """This property setter sets the data to a value which
        is an integer

        Arguments:
                value - the value of data which must be an integer
        TypeError:
                data must be an integer
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """This property retrieve the next node object of
        the linked list

        Returns: Node object
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """This property setter sets it to a Node object or None

        Arguments:
                value - Node object

        TypeError:
                next_node must be a Node object
        """
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """SinglyLinkedList class which defines a singly linked list by
    private instance attribute head (having no setter or getter)

    Attributes:
            __head - the first node of the linked list
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """This public instance method inserts a new node into the
        current sorted (increasing order) position in the list.

        Arguments:
               value - data to be used to create a new node
        """
        new_node = Node(value)
        head_ptr = self.__head

        if head_ptr is None:
            self.__head = new_node
            head_ptr = self.__head
            return None

        prev_ptr = None
        # This iterates over the entire linked list
        while head_ptr.next_node is not None:
            if head_ptr.data > value:
                break
            prev_ptr = head_ptr
            head_ptr = head_ptr.next_node

        # When the position to be replace is at index 0
        if head_ptr.data > value and prev_ptr is None:
            new_node.next_node = head_ptr
            self.__head = new_node

        # When the position to be replace is at any index but 0 or -1
        elif head_ptr.data > value and prev_ptr is not None:
            prev_ptr.next_node = new_node
            new_node.next_node = head_ptr

        # When the position to be replace is at index -1, i.e last
        else:
            head_ptr.next_node = new_node

    def __str__(self):
        head_ptr = self.__head
        if head_ptr is None:
            return ""
        while head_ptr.next_node is not None:
            val = head_ptr.data
            print("{}".format(val))
            head_ptr = head_ptr.next_node
        # This returns the last data to be printed
        return "{}".format(head_ptr.data)
