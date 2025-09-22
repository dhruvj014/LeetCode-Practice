# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None or head.next is None):
            return None
        slow = head
        fast = head
        prev = None
        ctr = 0
        while(fast.next is not None and fast.next.next is not None):
            prev = slow
            slow = slow.next
            fast = fast.next.next
            ctr += 2
        print("Fast is - "+str(fast))
        print("Ctr is - "+str(ctr))
        if(fast.next is None):
            prev.next = slow.next
        else:
            slow.next = slow.next.next
        return head