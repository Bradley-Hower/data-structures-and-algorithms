# Class 32 - Code Challenge - Tree Intersection

## Overview

Takes two binary trees as parameters. Using repeat_node(), locates any nodes found in both binary trees. Returns a list of node values found in both. Works with strings and integers.

## Approach & Efficiency

From first binary tree, hashes out values and sets them to a hashtable using the set() method. Runs through second binary tree, determines if second binary tree values are present in first binary tree by checking hashtable via the has() method. If the value is present, the values is appended to a list. The list is the returned after running through all nodes.

## Tests

Run `pytest` to confirm functionality.

1. Create virtual environment:  `python3 -m venv .venv`
2. Activate virtual environment: `source .venv/bin/activate`
3. Freeze requirements: `pip freeze > requirements.txt`
4. Install test: `pip install pytest`
5. Run test: pytest
