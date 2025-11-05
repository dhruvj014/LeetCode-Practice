class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        
        q = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for neighbours in adj[node]:
                indegree[neighbours] -= 1
                if indegree[neighbours] == 0:
                    q.append(neighbours)
        return topo if len(topo) == numCourses else []