from linked_list_pack.queue import Queue

class KaryTree():
  def __init__(self, root=None):
    self.root = root

  def breadth_first(self):
    """Traverses tree, adds current value to the output and queues any children for future traversal. If no children, continues."""
    if not self.root:
      return []

    queue = Queue()

    queue.enqueue(self.root)

    output = []

    while not queue.is_empty():
      current_node = queue.dequeue()
      output.append(current_node.value)
      for child in current_node.children:
        queue.enqueue(child)

    return output

  def clone(self):
    """Creates a clone of the input tree"""
    def traverse(source_node):
      if source_node is None:
        return

      clone_node = Node(source_node.value)

      for source_child in source_node.children:
        cloned_child = traverse(source_child)
        if cloned_child:
          clone_node.children.append(cloned_child)

      return clone_node

    cloned_tree = KaryTree()
    cloned_tree.root = traverse(self.root)
    return cloned_tree

class Node:
  """Node creation, sets incoming value to constructor self.value, points to any children nodes."""
  def __init__(self, value):
    self.value = value
    self.children = []
