from linked_list_pack.invalid_operation_error import InvalidOperationError


class Stack:
    """
    Contains identifier of top, has string generation output of linkedlist
    """

    def __init__(self):
        self.top = None

    """Can insert new node at top."""
    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
            return
        else:
            current_node = new_node
            current_node.next = self.top
            self.top = current_node

    """Can remove or 'pop' node from top."""
    def pop(self):
        current_node = self.top
        if current_node is None:
                    raise InvalidOperationError
        return_value = current_node.value
        self.top = current_node.next
        return return_value

    """Can view or 'peek' at node on top."""
    def peek(self):
        current_node = self.top
        if current_node is None:
            raise InvalidOperationError
        return current_node.value

    """Can see if stack is empty."""
    def is_empty(self):
        current_node = self.top
        if current_node is None:
            return True
        else:
            return False

class Node:
    "Creates new node. Node holds value and indicates next node linked to."
    def __init__(self, value):
        self.value = value
        self.next = None

