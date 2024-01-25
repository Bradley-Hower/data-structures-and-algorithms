# Class 08 - Code Challenge - Linked List Zip

Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node. Moreover, can return string printout of linked list and has validator to confirm if value is within linked list.

Insertion Additions:

Able to append to end of linked list, add a node before a specified node, after a specified node. Will raise exeption error if no node present for adding before or after node.

Kth place from the Value Additions:

Able to locate a node and return the value from k places from the tail. Raises errors if k places exceeds list lenghth or is less than zero.

Zipped:

Able to combine two lists in alternating fashion, regarding of differing lengths. Longer list's elements are appended to end.

## Whiteboard Process

![whiteboard_class06](codechallenge08.jpg)

## Approach & Efficiency

My approach was to simplify the process as much as possible by using a list. This way, it was clear what the total elements were and via simply sutraction, the location of the desired element could easily be located (adjust by one for indexing).

## Solution

Run `pytest` to confirm functionality.

Linked lists can be initialized with the following:

```
linked_list = LinkedList()
```
