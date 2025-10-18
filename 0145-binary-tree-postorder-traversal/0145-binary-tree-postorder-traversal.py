# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder = []
        if not root:
            return postorder
        st = []
        curr = root
        last_visited = None  # â ADDED: Track last visited node

        while curr or st:
            if curr:
                st.append(curr)
                curr = curr.left
            else:
                peek = st[-1]
                # â FIXED: Only go to right child if it exists and hasn't been visited
                if peek.right and last_visited != peek.right:
                    curr = peek.right
                else:
                    postorder.append(peek.val)
                    last_visited = st.pop()  # â FIXED: update last_visited
        return postorder