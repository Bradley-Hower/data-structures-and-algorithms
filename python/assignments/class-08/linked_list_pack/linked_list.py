class LinkedList:
    """
    Contains identifier of head, has string generation output of linkedlist
    """

    def __init__(self):
        self.head = None

    def __str__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(f'{{ {node.value} }}')
            node = node.next
        nodes.append("NULL")
        return " -> ".join(nodes)

    """Can insert new node at head."""
    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    """Rolls through nodes, can verify if a value is in linked list."""
    def includes(self, value):
        current_node = self.head
        while(current_node):
            if(value == current_node.value):
                return True
            current_node = current_node.next

    """Rolls through linked list until at end. Modifies linked list, adding new node to end"""
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        else:
            current_node = self.head
            while(current_node):
                if(current_node.next == None):
                    current_node.next = Node(value)
                    return
                else:
                    current_node = current_node.next

    """Selectively adds new node before a specified node, indicated by value. Raises exception if no nodes are present"""
    def insert_before(self, value, new_value):
        current_node = self.head
        previous_node = None
        if not current_node:
            raise TargetError
        while(current_node):
            if(value == current_node.value):
                new_node = Node(new_value)
                if previous_node is None:
                    new_node.next = self.head
                    self.head = new_node
                else:
                    previous_node.next = new_node
                    new_node.next = current_node
                return
            else:
                previous_node = current_node
                current_node = current_node.next
                if current_node is None:
                    raise TargetError

    """Selectively adds new node after a specified node, indicated by value. Raises exception if no nodes are present"""
    def insert_after(self, value, new_value):
        current_node = self.head
        if not current_node:
            raise TargetError
        while(current_node):
            if(value == current_node.value):
                new_node = Node(new_value)
                new_node.next = current_node.next
                current_node.next = new_node
                return
            else:
                current_node = current_node.next
                if current_node is None:
                    raise TargetError

    def delete(self, value):
        current_node = self.head
        previous_node = None
        if not current_node:
            raise TargetError
        while(current_node):
            if(value == current_node.value):
                if previous_node is None:
                    current_node.next = self.head
                    current_node.next = None
                    current_node.next = None
                else:
                    if current_node.next == None:
                        previous_node.next = None
                        current_node = None
                    else:
                        previous_node.next = current_node.next
                        current_node.next = None
                return
            else:
                previous_node = current_node
                current_node = current_node.next
                if current_node is None:
                    raise TargetError

    """Selects and return element from x places from the tail. If x is beyond range, raises TargetErrror."""
    def kth_from_end(self, kplaces):
        somelist_index = 0
        current_node = self.head

        # Creates total index numbers
        while(current_node is not None):
            somelist_index += 1
            current_node = current_node.next

        somelist_index -= 1
        node_number_select = somelist_index - kplaces

        # TargetErrors
        if somelist_index - kplaces < 0 :
            raise TargetError
        elif kplaces < 0:
            raise TargetError

        # Traverse linked list
        current_node = self.head
        current_node_number = 0
        while(current_node):
            if current_node_number == node_number_select:
                return current_node.value
            current_node_number += 1
            current_node = current_node.next

class Node:
    "Creates new node. Node holds value and indicates next node linked to."
    def __init__(self, value):
        self.value = value
        self.next = None

"""Raises exception error in case of exception"""
class TargetError(Exception):
    pass

