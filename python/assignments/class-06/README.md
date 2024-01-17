# Class 06 - Code Challenge - Linked List Insertions

Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node. Moreover, can return string printout of linked list and has validator to confirm if value is within linked list.

Insertion Additions:

Able to append to end of linked list, add a node before a specified node, after a specified node. Will raise exeption error if no node present for adding before or after node.

## Whiteboard Process

![whiteboard_class06](/codechallenge06.jpg)

## Approach & Efficiency

My approach to solving append was understanding that the end node needed to be located first before a node could be added. For the insert before and insert after, it was important to remeber to have the nodes always connected and not abandoned. For the exeption errors I needed some assistance with this from a TA, but once it was clarrified to be that the TargetError needed an exception argument and that the test showed that indeed, there was no node yet on the linked list, then the placing of the code was clear.

## Solution

Run `pytest` to confirm functionality.

Linked lists can be initialized with the following:

```
linked_list = LinkedList()
```

