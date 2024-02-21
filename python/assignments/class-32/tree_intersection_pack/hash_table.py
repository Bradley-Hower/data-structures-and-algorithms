from tree_intersection_pack.linked_list import LinkedList
from tree_intersection_pack.binary_tree import BinaryTree, Node

class Hashtable:
  """
  Defines buckets. Initiated as an empty array with range set to defined size (defaults to 1024).
  """
  def __init__(self, size=1024):
    self._size = size
    self._buckets = [None] * size

  """
  Hash function. Sets location of keys according to defined algorithm.
  Algorith:
    o Multiply ASCII value together.
    o Multiply by prime number, 599.
    o Modulo by hash size.
  """
  def _hash(self, key):
    index = 0
    for char in key:
      index *= ord(char)
    index *= 599
    index = index % self._size

    return index

  """
  If key already exists in array, locates it and replaces value. If value bucket is empty, adds a linked list to bucket.
  """
  def set(self, key, value):
    index = self._hash(key)
    bucket = self._buckets[index]

    if bucket is None:
      bucket = LinkedList()
      self._buckets[index] = bucket

    current = bucket.head

    while current:
      candidate = current.val
      if candidate[0] == key:
        candidate[1] = value
        return
      else:
        current = current.next

    kv_pair = [key, value]
    bucket.insert(kv_pair)

  """
  Searches array with given key, returns value if one exists, else returns None.
  """
  def get(self, key):
    index = self._hash(key)
    bucket = self._buckets[index]

    if bucket is None:
      return None

    current = bucket.head

    while current:
      kv_pair = current.val
      if kv_pair[0] == key:
        return kv_pair[1]

      current = current.next

    return None

  """
  Searches hash array if key exists. Returns a boolean accordingly.
  """
  def has(self,key):
    for bucket in self._buckets:
      if bucket:
        current = bucket.head
        while current:
          kv_pair = current.val
          if kv_pair[0] == key:
            return True

          current = current.next

  """
  Returns list of keys in hash array.
  """
  def keys(self):
    key_list = []

    for bucket in self._buckets:
      if bucket:
        current = bucket.head

        while current:
          kv_pair = current.val[0]
          key_list.append(kv_pair)
          current = current.next

    return key_list

  def repeat_hash(self, input_str):
    for word in input_str.split():
      word_nocommas = word.replace(',', '')
      word_lower = word_nocommas.lower()
      if self.has(word_lower):
        return word_lower
      else:
        self.set(word_lower, True)

  def repeat_node(self, tree1, tree2):
    tree1_list = tree1.pre_order()
    tree2_list = tree2.pre_order()

    common_node_values = []
    for e in tree1_list:
      self.set(str(e), True)

    for e in tree2_list:

      if self.has(str(e)):
        if isinstance(e, int):
          common_node_values.append(int(e))
        else:
          common_node_values.append(e)
      else:
        self.set(str(e), True)

    return common_node_values



