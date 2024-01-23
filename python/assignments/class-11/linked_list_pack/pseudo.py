from linked_list_pack.invalid_operation_error import InvalidOperationError

class PseudoQueue:
  def __init__(self):
    self.top = None

  """Can insert new node at top."""
  def enqueue(self, value):
    new_node = Node(value)
    if self.top is None:
      self.top = new_node
      return
    else:
      current_node = new_node
      current_node.next = self.top
      self.top = current_node


  def dequeue(self):
    current_node = self.top
    while current_node is not None:
      if current_node.next == None:
         return current_node.value
      elif current_node.next.next == None:
         temp = current_node.next
         current_node.next = None
         return temp.value
      current_node = current_node.next

class Node:
  "Creates new node. Node holds value and indicates next node linked to."
  def __init__(self, value):
    self.value = value
    self.next = None
