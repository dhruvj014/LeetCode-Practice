# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_width = 0
        q = deque()
        q.append((root,0))
        while q:
            size = len(q)
            min_index = q[0][1]
            first = 0
            last = 0
            for i in range(size):
                node, idx = q.popleft()
                curr_index = idx - min_index
                if i == 0:
                    first = curr_index
                if i == size - 1:
                    last = curr_index
                if node.left:
                    q.append((node.left, 
                              2 * curr_index + 1))
                if node.right:
                    q.append((node.right, 
                              2 * curr_index + 2))
            max_width = max(max_width, 
                            last - first + 1)
        return max_width
