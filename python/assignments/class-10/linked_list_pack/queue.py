from linked_list_pack.invalid_operation_error import InvalidOperationError

class Queue:
  """
  Contains identifier of top, has string generation output of linkedlist
  """

  def __init__(self):
    self.front = None
    self.rear = None

  def enqueue(self, value):
    new_node = Node(value)
    if self.rear == None:
      self.front = self.rear = new_node
      return
    current_node = self.rear
    current_node.next = new_node
    self.rear = new_node

  def dequeue(self):
    if self.rear is None and self.front is None:
      raise InvalidOperationError
    temp = self.front
    self.front = temp.next
    return temp.value

  def peek(self):
    current_front = self.front
    if self.front is None:
      raise InvalidOperationError
    return current_front.value

  def is_empty(self):
    if self.front is None or self.rear is None:
      return True
    else:
      return False

class Node:
    "Creates new node. Node holds value and indicates next node linked to."
    def __init__(self, value):
        self.value = value
        self.next = None



