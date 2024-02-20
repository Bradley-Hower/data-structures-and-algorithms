import pytest
from hash_table_pack.hash_table import Hashtable



def __init__(self):
    # initialization here
    pass

def some_method(self):
    # method body here
    pass

def test_exists():
    assert Hashtable

def test_repeat():
    hashtable = Hashtable()
    actual = hashtable.repeat_hash("apple pie apple")
    expected = "apple"
    assert actual == expected

def test_one():
    hashtable = Hashtable()
    actual = hashtable.repeat_hash("apple")
    expected = None
    assert actual == expected

def test_none():
    hashtable = Hashtable()
    actual = hashtable.repeat_hash("")
    expected = None
    assert actual == expected

def test_example_one():
    hashtable = Hashtable()
    actual = hashtable.repeat_hash("Once upon a time, there was a brave princess who...")
    expected = "a"
    assert actual == expected

def test_example_two():
    hashtable = Hashtable()
    actual = hashtable.repeat_hash("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...")
    expected = "it"
    assert actual == expected

def test_example_three():
    hashtable = Hashtable()
    actual = hashtable.repeat_hash("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...")
    expected = "summer"
    assert actual == expected
