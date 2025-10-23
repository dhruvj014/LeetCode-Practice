from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        nq = deque()
        nq.append(root)

        leftToRight = True

        while nq:
            size = len(nq)
            row = [0]*size
            for i in range(size):
                node = nq.popleft()
                index = i if leftToRight else (size - 1 - i)
                row[index] = node.val
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            leftToRight = not leftToRight
            res.append(row)
        return res