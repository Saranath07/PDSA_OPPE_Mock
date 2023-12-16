## Binary Search Tree

```python
class Node:
    def __init__(self,data):
    	# Contains reference to the left child node if it exists, otherwise None
        self.left = None 
        # Stores data
        self.data = data
        # Contains reference to the right child node if it exists, otherwise None
        self.right = None
```

Consider an implementation of a Binary Search Tree, where each node is created using the given class Node. Suppose it has a root variable that contains the reference to the root node of the binary search tree.

Complete the function insert_element(root, k) That accepts the reference of root node root of non-empty binary search tree and an integer k. The function insert the element k at the correct position of the binary search tree. The function does not print or return anything.

## Sample Input 1

```python
10 #root element
5 18 8 3 15 25 17 #Elements to be insert in bst in given order
```

## Output

```python
3 5 8 10 15 17 18 25 #Inorder
10 5 3 8 18 15 17 25 #Preorder
3 8 5 17 15 25 18 10 #Postorder
```

Explanation:- After insertion all element, following is the resultant BST