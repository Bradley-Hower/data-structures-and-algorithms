from hash_table_pack.hash_table import Hashtable

class HashRepeat:
  def repeat_hash(input_str):
    for word in input_str:
      if Hashtable.has(word):
        return word
      else:
        Hashtable.set(word, True)



