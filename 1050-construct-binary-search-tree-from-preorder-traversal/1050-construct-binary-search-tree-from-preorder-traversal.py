# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        i = 0
        def build(A,bound):
            nonlocal i
            if i == len(A) or A[i] > bound:
                return None
            root = TreeNode(A[i])
            i+=1
            root.left = build(A,root.val)
            root.right = build(A,bound)
            return root
        return build(preorder, sys.maxsize)