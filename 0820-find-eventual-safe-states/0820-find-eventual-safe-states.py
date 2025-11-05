class Solution:
    def dfs(self, node, adj, vis, pathvis,check):
        vis[node] = 1
        pathvis[node] = 1
        check[node] = 0
        for neighbour in adj[node]:
            if vis[neighbour] == 0:
                if self.dfs(neighbour, adj, vis, pathvis,check):
                    return True
            else:
                if pathvis[neighbour] == 1:
                    return True
        check[node] = 1
        pathvis[node] = 0
        return False
            
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        vis = [0]*V
        pathvis = [0]*V
        check = [0]*V
        for i in range(V):
            if vis[i]==0:
                self.dfs(i, graph, vis, pathvis,check)
        sol = []
        for i in range(V):
            if check[i] == 1:
                sol.append(i)
        return sol