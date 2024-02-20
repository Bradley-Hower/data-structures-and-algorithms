# Class 31 - Code Challenge - Hash Repeat Words

## Overview

Builds out hashtable functionality. Has set key, get value, and search if has key methods. Method for returning full hash array. Added function for reapeat hashes.

## Approach & Efficiency

Added funtionality, repeat_hash(). Returns first occuring reapeat of a word in a string composed of words. Function utilizes has() function to check if word has already appeared and been hashed. If none is located for a given word, the word is set to the hashtable, using the set() function.

## Tests

Run `pytest` to confirm functionality.

1. Create virtual environment:  `python3 -m venv .venv`
2. Activate virtual environment: `source .venv/bin/activate`
3. Freeze requirements: `pip freeze > requirements.txt`
4. Install test: `pip install pytest`
5. Run test: pytest
