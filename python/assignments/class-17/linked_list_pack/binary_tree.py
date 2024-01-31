class BinaryTree:
  """

  """
  def __init__(self):
    self.root = None

  def pre_order(self):
    """
          a
      b      c
    d  e    f  g

    ["a",       "b", "d", "e",      "c", "f", "g"]

    root -> left -> right
    BUT "root" depends on context
    It's not necessarily same as root of overall tree

    """

    def traverse(node):
      """
      task is

      return base result + left node's result + right node's result

      ["a"] + ["b","d","e"] + ["c","f","g"]

      return List

      """
      if node is None:
        return []

      base_result = [node.value]
      left_result = traverse(node.left)
      right_result = traverse(node.right)

      return base_result + left_result + right_result

    return traverse(self.root)

  def in_order(self):
    """
          a
      b      c
    d  e    f  g

    ["d",     "b",      "e",      "a",      "f",      "c",     "e"]
    left -> root -> right
    """

    def traverse(node):

      if node is None:
        return []

      left_result = traverse(node.left)
      base_result = [node.value]
      right_result = traverse(node.right)

      return left_result + base_result + right_result

    return traverse(self.root)

  def post_order(self):
    """
          a
      b      c
    d  e    f  g
    ["d", "e", "b"    "f", "g", "c"      "a"]
    left -> right -> root
    """

    def traverse(node):

      if node is None:
        return []

      left_result = traverse(node.left)
      right_result = traverse(node.right)
      base_result = [node.value]

      return left_result + right_result + base_result

    return traverse(self.root)

  def find_maximum_value(self):
    """Traverses the nodes, returns the max among them. Accomplishes this via recursion, max values are return up after comparison."""

    def traverse(node):
      if node is None:
        return float('-inf') #This part with the help of chatgpt

      left_result = traverse(node.left)
      base_result = node.value
      right_result = traverse(node.right)

      return max([left_result, right_result, base_result])


    return traverse(self.root)



class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

