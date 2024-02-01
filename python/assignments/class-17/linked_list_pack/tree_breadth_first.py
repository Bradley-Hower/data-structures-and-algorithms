from linked_list_pack.queue import Queue

def breadth_first(tree_node):
  """Traverses tree, adds current value to the output and queues any children for future traversal. If no children, continues."""
  if not tree_node.root:
    return []

  queue = Queue()

  queue.enqueue(tree_node.root)

  output = []

  while not queue.is_empty():
    print(queue)
    current_node = queue.dequeue()
    output.append(current_node.value)

    if current_node.left is not None:
      queue.enqueue(current_node.left)

    if current_node.right is not None:
      queue.enqueue(current_node.right)

  return output

