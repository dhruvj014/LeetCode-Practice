# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findMiddle(self, head: Optional[ListNode]):
        if head is None or head.next is None:
            return head
        slow = head
        fast = head.next
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def mergeLists(self,left: Optional[ListNode], right: Optional[ListNode]):
        dummy = ListNode(-1)
        temp = dummy
        while(left is not None and right is not None):
            if(left.val < right.val):
                temp.next = left
                temp = left
                left = left.next
            else:
                temp.next = right
                temp = right
                right = right.next
        if left:
            temp.next = left
        else:
            temp.next = right
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        mid= self.findMiddle(head)
        right = mid.next
        mid.next = None
        left = head

        left = self.sortList(left)
        right = self.sortList(right)
        return self.mergeLists(left,right)