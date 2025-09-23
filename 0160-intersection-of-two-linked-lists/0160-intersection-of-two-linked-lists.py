# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> Optional[ListNode]:
        if head1 is None or head2 is None:
            return None
        t1 = head1
        t2 = head2
        while(t1!=t2):
            t1 = t1.next
            t2 = t2.next
            if(t1 == t2):
                return t1
            if(t1 is None):
                t1 = head2
            if(t2 is None):
                t2 = head1
        return t1