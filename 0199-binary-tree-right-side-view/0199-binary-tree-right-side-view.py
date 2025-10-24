# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ds = []
        def calc(node, level):
            if not node:
                return
            if level == len(ds):
                ds.append(node.val)
            calc(node.right,level+1)
            calc(node.left,level+1)
        calc(root,0)
        return ds