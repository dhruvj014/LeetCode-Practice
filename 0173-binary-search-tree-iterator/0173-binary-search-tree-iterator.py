# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    st = []
    def pushAll(self, root):
        curr = root
        while curr:
            self.st.append(curr)
            curr = curr.left
    def __init__(self, root: Optional[TreeNode]):
        self.pushAll(root)

    def next(self) -> int:
        temp = self.st[-1]
        self.st.pop()
        self.pushAll(temp.right)
        return temp.val

    def hasNext(self) -> bool:
        return bool(self.st)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()