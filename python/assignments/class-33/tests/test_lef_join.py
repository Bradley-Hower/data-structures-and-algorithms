import pytest
from left_join_pack.binary_tree import BinaryTree, Node
from left_join_pack.hash_table import Hashtable

def test_synonym():
    hashtable = Hashtable()
    hashtable.set("diligent", "employed")
    hashtable.set("fond", "enamored")
    hashtable.set("guide", "usher")
    hashtable.set("outfit", "garb")
    hashtable.set("wrath", "anger")
    hashtable2 = Hashtable()
    hashtable_test = Hashtable()
    actual = hashtable_test.left_join(hashtable, hashtable2)
    expected = [['wrath','anger', None],['outfit','garb',None,],['guide','usher',None],['fond','enamored', None],['diligent','employed', None]]
    assert actual == expected

def test_antonym():
    hashtable = Hashtable()
    hashtable2 = Hashtable()
    hashtable2.set("diligent", "idle")
    hashtable2.set("fond", "averse")
    hashtable2.set("guide", "follow")
    hashtable2.set("flow", "jam")
    hashtable2.set("wrath", "delight")
    hashtable_test = Hashtable()
    actual = hashtable_test.left_join(hashtable, hashtable2)
    expected = []
    assert actual == expected

def test_left_join():
    hashtable = Hashtable()
    hashtable.set("diligent", "employed")
    hashtable.set("fond", "enamored")
    hashtable.set("guide", "usher")
    hashtable.set("outfit", "garb")
    hashtable.set("wrath", "anger")
    hashtable2 = Hashtable()
    hashtable2.set("diligent", "idle")
    hashtable2.set("fond", "averse")
    hashtable2.set("guide", "follow")
    hashtable2.set("flow", "jam")
    hashtable2.set("wrath", "delight")
    hashtable_test = Hashtable()
    actual = hashtable_test.left_join(hashtable, hashtable2)
    expected = [['wrath','anger','delight',],['outfit','garb',None,],['guide','usher','follow',],['fond','enamored','averse',],['diligent','employed','idle',]]
    assert actual == expected
