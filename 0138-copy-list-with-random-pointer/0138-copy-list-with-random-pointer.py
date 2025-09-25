"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Step 1
        if head is None:
            return head
        temp = head
        while(temp is not None):
            copy = Node(temp.val)
            copy.next = temp.next
            temp.next = copy
            temp = temp.next.next
        
        #Step 2
        temp = head
        while(temp is not None):
            copy = temp.next
            if temp.random:
                copy.random = temp.random.next
            else:
                copy.random = None
            temp = temp.next.next
        
        #Step 3
        dummy = Node(-1)
        res = dummy
        temp = head
        while(temp is not None):
            res.next = temp.next
            temp.next = temp.next.next
            res = res.next
            temp = temp.next
        return dummy.next
