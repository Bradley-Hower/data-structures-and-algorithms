# Class 18 - Code Challenge - FizzBuzz

Takes a clone of a K-ary tree by traversal and replaces values according to the rules of Fizz Buzz.

## Approach & Efficiency

Recognizing the clone method creates a copy, from that each node can be traversed through, just like a breadth first search. At first I was inclined to used a list for the ouput, but then I realized that the values could be changed in place. The tests then passed.

## Solution

See linked_list_pack/tree_fizz_buzz.

Run `pytest` to confirm functionality.

1. Creat virtual environment:  `python3 -m venv .venv`
2. Activate virtual environment: `source .venv/bin/activate`
3. Freeze requirements: `pip freeze > requirements.txt`
4. Install test: `pip install pytest`

Note, sometimes pytest needs to be uninstalled and reinstalled if it was previous installed under another directory.
