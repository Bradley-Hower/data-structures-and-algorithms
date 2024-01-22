# Class 10 - Code Challenge - Stack and Queue

Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.

## Approach & Efficiency

The tricky part was not abandoning a node. Once the points were establish in the proper order, everything passed. For queues, special attention when the queue is empty is needed to be sure both front and rear tags are in place.

## Solution

Run `pytest` to confirm functionality.

1. Creat virtual environment:  `python3 -m venv .venv`
2. Activate virtual environment: `source .venv/bin/activate`
3. Freeze requirements: `pip freeze > requirements.txt`
4. Install test: `pip install pytest`

Note, sometimes pytest needs to be uninstalled and reinstalled if it was previous installed under another directory.
