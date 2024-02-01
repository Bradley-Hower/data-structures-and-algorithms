from linked_list_pack.kary_tree import KaryTree, Node
from linked_list_pack.queue import Queue

def fizz_buzz_tree(tree):
  """Takes in a tree and uses clone method to create copy. From this clone, changes values of nodes according to the rules of Fizz Buzz."""
  cloned_tree = tree.clone()

  def traverse(source_code):

    queue = Queue()

    queue.enqueue(source_code.root)

    while not queue.is_empty():
      current_node = queue.dequeue()

      if current_node.value % 15 == 0:
        current_node.value = "FizzBuzz"
      elif current_node.value % 3 == 0:
        current_node.value = "Fizz"
      elif current_node.value % 5 == 0:
        current_node.value = "Buzz"
      else:
        current_node.value = str(current_node.value)

      for child in current_node.children:
        queue.enqueue(child)

  traverse(cloned_tree)
  return cloned_tree
