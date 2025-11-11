class Solution:
    timer = 1
    def dfs(self,node,parent,vis, adj, tin, low, bridges):
            vis[node] = 1
            tin[node] = self.timer
            low[node] = self.timer
            self.timer += 1
            for it in adj[node]:
                if it == parent:
                    continue
                if vis[it] == 0:
                    self.dfs(it,node,vis,adj,tin,low,bridges)
                    low[node] = min(low[node],low[it])
                    if low[it] > tin[node]:
                        bridges.append([it,node])
                else:
                    low[node] = min(low[node],low[it])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        vis = [0 for _ in range(n)]
        low = [0 for _ in range(n)]
        tin = [0 for _ in range(n)]
        bridges = []
        self.dfs(0, -1,vis, adj, tin, low, bridges)
        return bridges