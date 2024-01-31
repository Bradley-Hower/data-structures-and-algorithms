def breadth_first(tree_node):
  """Traverses tree, adds current value to the output and queues any children for future traversal. If no children, continues."""
  if not tree_node.root:
    return []

  queue = [tree_node.root]

  output = []

  while(len(queue) > 0):
    current_node = queue.pop(0)
    output.append(current_node.value)

    if current_node.left is not None:
      queue.append(current_node.left)

    if current_node.right is not None:
      queue.append(current_node.right)

  return output

