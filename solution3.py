class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeSortedList(head1, head2):
    if head1 is None:
        return head2
    
    if head2 is None:
        return head1
    
    if head1.data < head2.data:
        head = head1
        head1 = head1.next
    
    else:
        head = head2
        head2 = head2.next
    
    temp = head
    while head1.next != None and head2.next != None:
        if head1.data < head2.data:
            temp.next = head1
            head1 = head1.next
        
        else:
            temp.next = head2
            head2 = head2.next
        
        temp = temp.next
    
    if head1 != None:
        temp.next = head1
    
    else:
        temp.next = head2
    
    return head
            

    
