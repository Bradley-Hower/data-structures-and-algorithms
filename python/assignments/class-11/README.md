# Class 11 - Code Challenge - Pseudo Stack Queue

Creating a pseduo queue by only using two stacks, no queues.

## Whiteboard Process

![whiteboard_class11](/codechallenge11.jpg)

## Approach & Efficiency

My tought of how to approach this is to push all values to the first stack and then pop thenm to the next stack, and then pop them from the second stack. This would effectively flip the stack and allow us to pull from the bottom.

## Solution

Run `pytest` to confirm functionality.

1. Creat virtual environment:  `python3 -m venv .venv`
2. Activate virtual environment: `source .venv/bin/activate`
3. Freeze requirements: `pip freeze > requirements.txt`
4. Install test: `pip install pytest`

Note, sometimes pytest needs to be uninstalled and reinstalled if it was previous installed under another directory.
