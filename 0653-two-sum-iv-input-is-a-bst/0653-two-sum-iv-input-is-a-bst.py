# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def pushAll(self, root):
        node = root
        while node:
            self.st.append(node)
            node = node.right if self.reverse else node.left

    def __init__(self, root: Optional[TreeNode], isReverse: bool):
        self.st = []
        self.reverse = isReverse
        self.pushAll(root)

    def next(self) -> int:
        temp = self.st[-1]
        self.st.pop()
        if not self.reverse: 
            self.pushAll(temp.right)
        else:
            self.pushAll(temp.left)    
        return temp.val

    def hasNext(self) -> bool:
        return bool(self.st)

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        l = BSTIterator(root, False)
        r = BSTIterator(root, True)

        i = l.next()
        j = r.next()
        while(i<j):
            if i + j == k:
                return True
            elif i + j < k:
                i = l.next()
            else:
                j = r.next()
        return False