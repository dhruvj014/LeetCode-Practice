class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        dist = [sys.maxsize] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        
        # Min-heap: (distance, node)
        pq = [(0, 0)]
        mod = int(1e9 + 7)
        
        while pq:
            dis, node = heapq.heappop(pq)
            
            # Skip outdated distances
            if dis > dist[node]:
                continue
            
            for adjNode, wt in adj[node]:
                newDist = dis + wt
                
                if newDist < dist[adjNode]:
                    dist[adjNode] = newDist
                    ways[adjNode] = ways[node]
                    heapq.heappush(pq, (newDist, adjNode))
                
                # Found another shortest path to adjNode
                elif newDist == dist[adjNode]:
                    ways[adjNode] = (ways[adjNode] + ways[node]) % mod
        
        return ways[n - 1] % mod