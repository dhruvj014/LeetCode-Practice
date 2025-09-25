# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findTail(self, temp):
        ctr = 1
        while temp.next is not None:
            ctr+=1
            temp = temp.next
        return temp,ctr
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        temp = head
        tail,n = self.findTail(temp)
        tail.next = head
        k = k%n
        target = n-k-1
        temp = head
        while(target>0):
            target-=1
            temp = temp.next
        head = temp.next
        temp.next = None
        return head