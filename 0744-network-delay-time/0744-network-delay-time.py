class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        for u, v, w in times:
            adj[u].append((v, w))
        
        dist = [sys.maxsize]*(n+1)
        dist[k] = 0
        
        pq = [(0, k)]
        
        while pq:
            dis, node = heapq.heappop(pq)
            
            if dis > dist[node]:
                continue
            
            for neighbour, wt in adj[node]:
                new_dist = dis + wt
                print("at node - "+str(node)+" and neighbour - "+str(neighbour)+ " with wt "+str(wt))
                if new_dist < dist[neighbour]:
                    dist[neighbour] = new_dist
                    heapq.heappush(pq,(new_dist, neighbour))
        
        maxi = 0
        print(dist)
        for i in range(1,len(dist)):
            maxi = max(maxi,dist[i])
        if maxi == sys.maxsize:
            return -1
        return maxi