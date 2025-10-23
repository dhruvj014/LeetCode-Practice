# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = float('-inf')
        self.dfs(root)
        return self.maxi
        
    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lsum = max(0, self.dfs(root.left))
        rsum = max(0, self.dfs(root.right))
        self.maxi = max(self.maxi, lsum + rsum + root.val)
        return root.val + max(lsum, rsum)