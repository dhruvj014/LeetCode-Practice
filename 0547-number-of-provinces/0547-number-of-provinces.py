class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def findParent(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def unionBySize(self, u, v):
        pu, pv = self.findParent(u), self.findParent(v)
        if pu == pv:
            return
        if self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        ds = DisjointSet(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    ds.unionBySize(i,j)
        ctr = 0
        for i in range(n):
            if ds.findParent(i) == i:
                ctr+=1
        return ctr