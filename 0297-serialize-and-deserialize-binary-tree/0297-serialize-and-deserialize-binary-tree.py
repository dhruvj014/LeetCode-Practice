# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue
from typing import Optional
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        s = ""
        q = Queue()
        q.put(root)
        while not q.empty():
            curr = q.get()
            if not curr:
                s += "#,"
            else:
                s += str(curr.val) + ","
                q.put(curr.left)
                q.put(curr.right)
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        q = Queue()
        tokens = data.split(",")
        root_val = int(tokens.pop(0))
        root = TreeNode(root_val)
        q.put(root)
        while not q.empty():
            curr = q.get()
            left_val = tokens.pop(0)
            print("currently left_val is "+left_val)
            if left_val == "#":
                curr.left = None
            else:
                left_node = TreeNode(int(left_val))
                curr.left = left_node
                q.put(left_node)
            
            right_val = tokens.pop(0)
            if right_val == "#":
                curr.right = None
            else:
                right_node = TreeNode(int(right_val))
                curr.right = right_node
                q.put(right_node)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))