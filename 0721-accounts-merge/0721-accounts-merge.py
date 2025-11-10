class DisjointSet:
	def __init__(self, n):
		self.rank = [0]*(n+1)
		self.parent = [i for i in range(n+1)]
		self.size = [1 for i in range(n+1)]
		
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        ds = DisjointSet(n)
        mapNode = {}
        for i in range(n):
            for j in range(1, len(accounts[i])):
                mail = accounts[i][j]
                if mail not in mapNode:
                    mapNode[mail] = i
                else:
                    ds.unionBySize(i, mapNode[mail])
        mergedMail = [[] for _ in range(n)]
        for mail, parent in mapNode.items():
            node = ds.findParent(parent)
            mergedMail[node].append(mail)
        
        ans = []
        for i in range(n):
            if len(mergedMail[i]) == 0:
                continue
            mergedMail[i].sort()
            temp = []
            temp.append(accounts[i][0])
            for i in mergedMail[i]:
                temp.append(i)
            # print("temp - "+str(temp))
            ans.append(temp)
        return ans