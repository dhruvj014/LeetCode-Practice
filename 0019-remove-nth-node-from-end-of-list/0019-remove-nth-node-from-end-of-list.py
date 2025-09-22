# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        first = head
        second = head
        for i in range(n):
            second = second.next
        if(second is None):
            return head.next
        while(second.next is not None):
            first = first.next
            second = second.next
        print("First is at - "+str(first))
        first.next = first.next.next
        return head 
        
        