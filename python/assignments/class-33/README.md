# Class 33 - Code Challenge - Left Join

## Overview

Takes two hashmaps as arugments. All keys and values from the synonym hash table are added. Values from the antonym hash table are appended if the hold a key that is also found in the synonym hash table. Key-value pairs only found in the antonym hash table are ignored.

## Approach & Efficiency

Utilizes get() meth to determine if key is present in hashtable. Processes accordingly if hashtable1 or hashtable2. If key does not exist in hashtable2, None is appended.

## Tests

Run `pytest` to confirm functionality.

1. Create virtual environment:  `python3 -m venv .venv`
2. Activate virtual environment: `source .venv/bin/activate`
3. Freeze requirements: `pip freeze > requirements.txt`
4. Install test: `pip install pytest`
5. Run test: pytest
