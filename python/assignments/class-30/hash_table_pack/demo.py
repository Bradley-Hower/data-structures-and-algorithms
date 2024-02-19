from x import LinkedList

class Hashtable:
  """
  docstring
  """

  def __init__(self, size=1024):
    self._size = size
    self._buckets = [None] * size

  def set(self, key, value):
    index = self._hash(key)
    bucket = self._buckets[index]

    if bucket is None:
      bucket = LinkedList()
      self._buckets[index] = bucket

    current = bucket.head

    while current:
      candidate = current.value
      if candidate[0] == key:
        # found existing
        candidate[1] = value
        return

    kv_pair = [key, value] # create new kv_pair due to not existing
    bucket.insert(kv_pair)

  def get(self, key):
    index = self._hash(key)
    bucket = self._buckets[index]

    if bucket is None:
      return None

    current = bucket.head

    while current:
      kv_pair = current.value
      if kv_pair[0] == key:
        return kv_pair[1]

      current = current.next

    raise KeyError("Unable to find key: ", key)

  def _hash(self, key):
    """
    x Add or multiply all the ASCII values together.
    x Multiply it by a prime number such as 599.
    Use modulo to get the remainder of the result, when divided by the total size of the array.
    """
    index = 0
    for char in key:
      index += ord(char)
    index *= 599
    index = index % self.size

    return index

  def keys(self):
    """
    return list of keys
    """
    key_list = []

    for bucket in self._buckets:
      if bucket: # linked list to traverse
        current = bucket.head
        while current:
          kv_pair = current.value[0]
          key_list.append(kv_pair)
          current = current.next

    return key_list

  def has(self, key):
    for bucket in self._buckets:
      if bucket:
        current = bucket.head
        while current:
          kv_pair = current.value
          if kv_pair[0] == key:
            return True

          current = current.next

