class DisjointSet:
	def __init__(self, n):
		self.rank = [0]*n
		self.parent = [i for i in range(n)]
		self.size = [1 for i in range(n)]
		
	def findParent(self, node):
		if node == self.parent[node]:
			return node
		self.parent[node] = self.findParent(self.parent[node])
		return self.parent[node]
		
	def unionByRank(self, u,v):
		pu = self.findParent(u)
		pv = self.findParent(v)
		if pu == pv:
			return
		if self.rank[pu] < self.rank[pv]:
			self.parent[pu] = pv
		elif self.rank[pv]<self.rank[pu]:
			self.parent[pv] = pu
		else:
			self.parent[pv] = pu
			self.rank[pu]+=1
			
	def unionBySize(self,u,v):
		pu = self.findParent(u)
		pv = self.findParent(v)
		if pu == pv:
			return
		if self.size[pu] < self.size[pv]:
			self.parent[pu] = pv
			self.size[pv] += self.size[pu]
		else:
			self.parent[pv] = pu
			self.size[pu] += self.size[pv]

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        ds = DisjointSet(n)
        ctr = 0
        for u,v in connections:
            if ds.findParent(u) == ds.findParent(v):
                ctr += 1
            else:
                ds.unionBySize(u,v)
        comp = 0
        for i in range(n):
            if ds.parent[i] == i:
                comp += 1
        if ctr >= comp - 1:
            return comp - 1
        return -1