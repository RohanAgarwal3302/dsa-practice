# Given the head of a linked list, 
# remove the nth node from the end of the list and return its head.

# head = [1,2,3,4,5], n = 2
# ans: [1,2,3,5]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# completed

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    
    def lenght(head):
        l=0
        cur_node=head
        while cur_node!=None:
            l+=1
            cur_node=cur_node.next
        return l

    index=lenght(head)-(n)
      
    # print(index)
    if index==0:
        head=head.next
        if head.val==None:
            return
        return head
    
    position=0
    current_node=head
      
    while position<(index-1):
        position+=1
        current_node=current_node.next
    
    if current_node.next==None:
        return head
    else:
        current_node.next=current_node.next.next
    return head