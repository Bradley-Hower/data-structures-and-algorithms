class LinkedList:
    """
    Contains identifier of head, has string generation output of linkedlist, can insert new node and verify if a value is in linked list.
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

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def includes(self, value):
        current_node = self.head
        while(current_node):
            if(value == current_node.value):
                return True
            current_node = current_node.next

class Node:
    "Holds value and indicates next node"
    def __init__(self, value):
        self.value = value
        self.next = None

class TargetError:
    try:
        LinkedList.includes()
        LinkedList.insert()
    except TypeError:
        print("Error. Don't forget to pass a value in. Can not process without one.")

