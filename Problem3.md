# Merge 2 Sorted Linked List

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

Consider an implementation of a linked list, where each node is created using the given class Node. Suppose it has a head variable that contains the reference to the first node of the linked list.

![Screenshot from 2023-12-08 12-15-43.png](https://s2.loli.net/2023/12/08/axTnel7g9HfBCWq.png)

You are given two non-empty linked lists with n and m nodes, where these nodes are sorted in ascending order of their value. Your task is to merge these two sorted linked lists into one sorted linked list.

Write a function mergeSortedList(head1, head2), where head1 and head2 are references to the first nodes of two sorted linked lists. The function should return the reference of the first node of the merged sorted linked list.

## Sample input
```
1 3 5 7 9 11     # Elements of first linked list
2 4 6            # Elements of second linked list
```

## Output
```
Output Linked List: 1 2 3 4 5 6 7 9 11 # Elements of merged sorted linked list
```