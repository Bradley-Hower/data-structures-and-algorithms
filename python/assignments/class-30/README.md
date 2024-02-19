# Class 30 - Code Challenge - Hash Tables

## Overview

Builds out hashtable functionality. Has set key, get value, and search if has key methods. Method for returning full hash array.

## Approach & Efficiency

Hashing method with algorithm which uses following seps in algorithm:

- Multiply ASCII value together.
- Multiply by prime number, 599.
- Modulo by hash size.

Utilizes linked lists in case of collisions. Values associated with any given key are cleared when setting if key is already present in linked list.

## Tests

Run `pytest` to confirm functionality.

1. Create virtual environment:  `python3 -m venv .venv`
2. Activate virtual environment: `source .venv/bin/activate`
3. Freeze requirements: `pip freeze > requirements.txt`
4. Install test: `pip install pytest`
5. Run test: python3 pytest
