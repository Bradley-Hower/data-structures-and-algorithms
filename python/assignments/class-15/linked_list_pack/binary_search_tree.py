from linked_list_pack.binary_tree import BinaryTree, Node

class BinarySearchTree(BinaryTree):
  """Pulls in the constructor from the partent"""
  def __init__(self):
    super().__init__()

  """Takes a given value and adds it to the tree. If there is no root, adds it to the root. Otherwise, if is less than the value, is pushed left. If is greater or equal to the value, pushed right. If ends at a empty node, value is added."""
  def add(self, value):
    """"""
    new_node = Node(value)

    if self.root == None:
      self.root = new_node
      return

    def traverse(node_to_check, node_to_add):
      if node_to_check.value > node_to_add.value:
        if node_to_check.left == None:
          node_to_check.left = node_to_add
        else:
          traverse(node_to_check.left, node_to_add)
      elif node_to_check.value <= node_to_add.value:
        if node_to_check.right == None:
          node_to_check.right = node_to_add
        else:
          traverse(node_to_check.right, node_to_add)

    traverse(self.root, new_node)

  def contains(self, value):
    """Evaliates current node and returns true. Firstly, checks if node is none. This is important, otherwise subsequent checks can not run. Then evaluates. If the node is less than the value, search continues right. If the node is greater than the value, the search continues left. Search continues in a recursive fassion until the node value is equal to the value and thus returns true. If a all recussions come up without, the final search will have been a search at an empty node and the final return will be false."""
    if self.root == value:
      return True

    def search(node_to_check, value):
      if node_to_check == None:
        return False
      if node_to_check.value > value:
        return search(node_to_check.left, value)
      elif node_to_check.value < value:
        return search(node_to_check.right, value)
      elif node_to_check.value == value:
        return True

    return search(self.root, value)
