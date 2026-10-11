class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        adj=[[] for i in range(n)]
        for u,v in connections:
            adj[u].append((v,1))
            adj[v].append((u,0))
        vis=[False]*n
        def dfs(node):
            c=0
            vis[node]=True
            for v,w in adj[node]:
                if not vis[v]:
                    c=c+w
                    c=c+dfs(v)
            return c
        
        return (dfs(0))