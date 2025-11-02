class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def mydfs(node):
            visited[node] = 1
            print("for node - "+str(node)+" the neighbours are "+str(adj[node]))
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    mydfs(neighbour)
        n = len(isConnected[0])
        prov = 0
        
        adj = [[] for _ in range(n)]
        for i in range(len(isConnected)):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    adj[i].append(j)
                    adj[j].append(i)

        visited = [0]*n
        for i in range(n):
            if visited[i] == 0:
                mydfs(i)
                prov += 1
        return prov