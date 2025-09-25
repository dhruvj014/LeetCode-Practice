# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self, temp):
        prev = None
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev
    def findknode(self,temp,k):
        k-=1
        while(temp is not None and k>0):
            k-=1
            temp = temp.next
        return temp
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        while(temp is not None):
            knode = self.findknode(temp,k)
            if knode is None:
                if(prevnode):
                    prevnode.next = temp
                break
            nextnode = knode.next
            knode.next = None
            self.reverseLL(temp)
            if(temp == head):
                head = knode
            else:
                prevnode.next = knode
            prevnode = temp
            temp = nextnode
        return head