# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode]):
        if (head == None or head.next == None):
            return head
        newHead = self.reverse(head.next)
        front = head.next
        front.next = head
        head.next = None
        return newHead

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while(fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        newHead = self.reverse(slow.next)
        first = head
        second = newHead
        while(second != None):
            if(first.val != second.val):
                self.reverse(newHead)
                return False
            first = first.next
            second = second.next
        self.reverse(newHead)
        return True