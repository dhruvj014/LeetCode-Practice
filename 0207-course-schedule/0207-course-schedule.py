class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[u].append(v)
            indegree[v] += 1
        
        q = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                
        ctr = 0
        while q:
            node = q.popleft()
            ctr += 1
            for neighbours in adj[node]:
                indegree[neighbours] -= 1
                if indegree[neighbours] == 0:
                    q.append(neighbours)
        return ctr == numCourses