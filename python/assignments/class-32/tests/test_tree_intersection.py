import pytest
from tree_intersection_pack.binary_tree import BinaryTree, Node
from tree_intersection_pack.hash_table import Hashtable

def test_pre_order(tree1):
    actual = tree1.pre_order()
    expected = ["a", "b", "d", "e", "c", "f", "g"]
    assert actual == expected

def test_intersection(tree1, tree2):
    hashtable = Hashtable()
    actual = hashtable.repeat_node(tree1, tree2)
    expected = ["a", "c", "f", "g"]
    assert actual == expected

def test_intersection2(tree3, tree4):
    hashtable = Hashtable()
    actual = hashtable.repeat_node(tree3, tree4)
    expected = [100,160,125,175,200,350,500]
    assert actual == expected

@pytest.fixture
def tree1():
    """
          a
      b      c
    d  e    f  g
    """

    tree1 = BinaryTree()

    tree1.root = Node("a")
    tree1.root.left = Node("b")
    tree1.root.right = Node("c")
    tree1.root.left.left = Node("d")
    tree1.root.left.right = Node("e")
    tree1.root.right.left = Node("f")
    tree1.root.right.right = Node("g")

    return tree1

@pytest.fixture
def tree2():
    """
          a
      2      c
    3  4    f  g
    """

    tree2 = BinaryTree()

    tree2.root = Node("a")
    tree2.root.left = Node("2")
    tree2.root.right = Node("c")
    tree2.root.left.left = Node("3")
    tree2.root.left.right = Node("4")
    tree2.root.right.left = Node("f")
    tree2.root.right.right = Node("g")

    return tree2

@pytest.fixture
def tree3():
    """
          150
      100         250
    75  160     200  350
       125 175     300 500
    """

    tree3 = BinaryTree()

    tree3.root = Node(150)
    tree3.root.left = Node(100)
    tree3.root.right = Node(250)
    tree3.root.left.left = Node(75)
    tree3.root.left.right = Node(160)
    tree3.root.right.left = Node(200)
    tree3.root.right.right = Node(350)
    tree3.root.left.right.left = Node(125)
    tree3.root.left.right.right = Node(175)
    tree3.root.right.right.left = Node(300)
    tree3.root.right.right.right = Node(500)

    return tree3

@pytest.fixture
def tree4():
    """
          42
      100         600
    15  160     200  350
       125 175       4 500
    """

    tree4 = BinaryTree()

    tree4.root = Node(42)
    tree4.root.left = Node(100)
    tree4.root.right = Node(600)
    tree4.root.left.left = Node(15)
    tree4.root.left.right = Node(160)
    tree4.root.right.left = Node(200)
    tree4.root.right.right = Node(350)
    tree4.root.left.right.left = Node(125)
    tree4.root.left.right.right = Node(175)
    tree4.root.right.right.left = Node(4)
    tree4.root.right.right.right = Node(500)

    return tree4
