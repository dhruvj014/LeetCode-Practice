class Solution:            
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        adjRev = [[] for _ in range(V)]
        indegree = [0] * V

        for i in range(V):
            for it in graph[i]:
                adjRev[it].append(i)
                indegree[i] += 1

        q = deque()
        safeNodes = []

        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            safeNodes.append(node)
            for it in adjRev[node]:
                indegree[it] -= 1
                if indegree[it] == 0:
                    q.append(it)

        safeNodes.sort()
        return safeNodes