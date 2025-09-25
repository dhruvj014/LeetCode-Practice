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
        if head is None:
            return head
        temp = head
        hashmap = {}
        while(temp is not None):
            newNode = Node(temp.val)
            hashmap[temp] = newNode
            temp = temp.next
        temp = head
        while(temp is not None):
            copy = hashmap[temp]
            copy.next = hashmap[temp.next] if temp.next is not None else None
            copy.random = hashmap[temp.random] if temp.random is not None else None
            temp = temp.next
        return hashmap[head]
