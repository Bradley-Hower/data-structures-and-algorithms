from linked_list_pack.invalid_operation_error import InvalidOperationError
from linked_list_pack.stack import Stack

class PseudoQueue:
  def __init__(self):
    self.instack = Stack()
    self.outstack = Stack()

  """Can insert new node at top."""
  def enqueue(self, value):
    self.instack.push(value)

  def dequeue(self):
    while not self.instack.is_empty():
      popped = self.instack.pop()
      self.outstack.push(popped)
    dequeued_value = self.outstack.pop()

    while not self.outstack.is_empty():
      popped = self.outstack.pop()
      self.instack.push(popped)

    return dequeued_value

class Node:
  "Creates new node. Node holds value and indicates next node linked to."
  def __init__(self, value):
    self.value = value
    self.next = None
