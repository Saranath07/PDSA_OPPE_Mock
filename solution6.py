class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
def insert_element(root,k):

    # Check availability 
    if root == None:
        root = Node(k)
        
    if k < root.data:
        if root.left == None:
            root.left = Node(k)
        else:
            insert_element(root.left, k)
    
    if k > root.data:
        if root.right == None:
            root.right = Node(k)
        else:
            insert_element(root.right, k)
    
    
    
        
    