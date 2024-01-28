from linked_list_pack.binary_tree import BinaryTree, Node

class BinarySearchTree(BinaryTree):
  def __init__(self):
    super().__init__()


  def add(self, value):
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
