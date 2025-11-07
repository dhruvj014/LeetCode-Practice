class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for flight in flights:
            adj[flight[0]].append((flight[1],flight[2]))
        q = collections.deque()
        q.append((0,src,0))
        dist = [sys.maxsize]*n
        dist[src] = 0
        while q:
            stops,node,dis = q.popleft()
            if stops>k:
                continue
            for neighbours in adj[node]:
                neighbour = neighbours[0]
                wt = neighbours[1]
                if dis + wt < dist[neighbour] and stops<=k:
                    dist[neighbour] = dis + wt
                    q.append((stops+1,neighbour,dist[neighbour]))
        if dist[dst] == sys.maxsize:
            return -1
        return dist[dst]