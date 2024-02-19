import pytest
from hash_table_pack.hash_table import Hashtable

def __init__(self):
    # initialization here
    pass

def some_method(self):
    # method body here
    pass

# @pytest.mark.skip("TODO")
def test_exists():
    assert Hashtable

# Note: breaking encapsulation
# @pytest.mark.skip("TODO")

"""
#7 Tests if hash puts key in size range.
"""
def test_hash():
    hashtable = Hashtable()
    actual = hashtable._hash("Zach")
    assert 0 <= actual < hashtable._size

# Note: breaking encapsulation

# @pytest.mark.skip("TODO")
def test_hash_twice():
    hashtable = Hashtable()
    first = hashtable._hash("Zach")
    second = hashtable._hash("Zach")
    assert first == second

"""
#1 and #2 Successfully returns value for key-value which was set.
"""

# @pytest.mark.skip("TODO")
def test_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "make a pie")
    actual = hashtable.get("apple")
    expected = "make a pie"
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_apple_again():
    hashtable = Hashtable()
    hashtable.set("apple", "make a pie")
    hashtable.set("apple", "red fruit")
    actual = hashtable.get("apple")
    expected = "red fruit"
    assert actual == expected

"""
#3 Successfully returns None if key was never set.
"""
# @pytest.mark.skip("TODO")
def test_key_not_exist():
    hashtable = Hashtable()
    actual = hashtable.get("unreal key")
    expected = None
    assert actual == expected

# @pytest.mark.skip("TODO")

def test_key_not_exist_again():
    """
    cat and act must be same hash
    """
    hashtable = Hashtable()
    hashtable.set("cat", "meow")
    actual = hashtable.get("act")
    expected = None
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_set():
    hashtable = Hashtable()
    hashtable.set("apple", "make a pie")
    hashtable.set("pineapple", "tropical delight")
    assert hashtable.has("apple")
    assert hashtable.has("pineapple")
    assert not hashtable.has("grape")

"""
#4 Successfully returns list of keys in hashtable upon setting and then running keys method.
"""

def test_keys():
    hashtable = Hashtable()
    hashtable.set("apple", "make a pie")
    hashtable.set("pineapple", "tropical delight")
    actual = hashtable.keys()
    expected = ["pineapple", "apple"]
    assert actual == expected

"""
#5 and #6 Tests for linked list functionality, given two keys that result in a collision. Successfully retrieves value.
"""

def test_collision_first():
    hashtable = Hashtable()
    hashtable.set("2Z", "make a pie")
    hashtable.set("Z2", "pink lady")
    actual = hashtable.get("2Z")
    expected = "make a pie"
    assert actual == expected

def test_collision_second():
    hashtable = Hashtable()
    hashtable.set("2Z", "make a pie")
    hashtable.set("Z2", "pink lady")
    actual = hashtable.get("Z2")
    expected = "pink lady"
    assert actual == expected
