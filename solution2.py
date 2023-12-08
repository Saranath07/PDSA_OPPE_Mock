class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def display(self, head):
        while head != None:
            print(head.data)
            head = head.next

def removeDuplicate(head):
    if head is None:
        return None
    
    temp = head
    while temp.next != None:
        if temp.data == temp.next.data:
            temp.next = temp.next.next
        else:
            temp = temp.next
    
    return head

L1 = Node(5)
L1.next = Node(10)
L1.next.next = Node(10)
L1.next.next.next = Node(20)

L1.display(removeDuplicate(L1))
