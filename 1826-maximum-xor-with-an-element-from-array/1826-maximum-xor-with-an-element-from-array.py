class Node:
    def __init__(self):
        self.links = [None, None]

    def containsKey(self, ind):
        return self.links[ind] is not None

    def get(self, ind):
        return self.links[ind]

    def put(self, ind, node):
        self.links[ind] = node

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if not node.containsKey(bit):
                node.put(bit, Node())
            node = node.get(bit)
    
    def findMax(self,num):
        node = self.root
        maxxor = 0
        for i in range(31,-1,-1):
            bit = (num>>i) & 1
            if node.containsKey(1-bit):
                maxxor = maxxor | (1<<i)
                node = node.get(1 - bit)
            else:
                node = node.get(bit)
        return maxxor

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        offlineQueries = []
        for index, (x, m) in enumerate(queries):
            offlineQueries.append((m, x, index))
        offlineQueries.sort()
        ans = [0]*len(queries)
        t = Trie()
        
        i = 0
        n = len(nums)

        for m,x,index in offlineQueries:
            while i < n and nums[i]<=m:
                t.insert(nums[i])
                i+=1
            if i != 0:
                ans[index] = t.findMax(x)
            else:
                ans[index] = -1
        return ans