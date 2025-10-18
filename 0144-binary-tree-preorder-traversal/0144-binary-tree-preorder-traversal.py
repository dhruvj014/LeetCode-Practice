# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        if root is None:
            return preorder
        st = []
        st.append(root)
        while st:
            node = st[-1]
            st.pop()
            preorder.append(node.val)
            if node.right is not None:
                st.append(node.right)
            if node.left is not None:
                st.append(node.left)
        return preorder               