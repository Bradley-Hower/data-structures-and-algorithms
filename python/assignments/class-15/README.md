# Class 15 - Code Challenge - Data Trees

In this challenge handles the building and traversing of a binary search tree (BST). For the traversal methods in the bindary tree, pre-order, in-order, and post-order are used. These methods handle how a traversal is handled, the directions within the structure to traverse. The Binary Search Tree class then contains methods to add and search for a given value. Binary trees are great because they are incredibly efficient, with a big O of O(log n).

## Approach & Efficiency

My approach was to take the process used in adding a value and modifying it to handle retreival. Two things were needed to accomplish this: One, checking if the current node was None. Secondaly, returning booleans *and* recursive functions.

## Solution

Run `pytest` to confirm functionality.

1. Creat virtual environment:  `python3 -m venv .venv`
2. Activate virtual environment: `source .venv/bin/activate`
3. Freeze requirements: `pip freeze > requirements.txt`
4. Install test: `pip install pytest`

Note, sometimes pytest needs to be uninstalled and reinstalled if it was previous installed under another directory.
