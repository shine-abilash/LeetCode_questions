class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n=len(edges)
        adj=[[] for i in range(n+1)]
        def dfs(node,tar,vis):
            vis[node]=True
            if node==tar:
                return True
            for v in adj[node]:
                if not vis[v]:
                    if dfs(v,tar,vis):
                        return True
            return False

        for u,v in edges:
            vis=[False]*(n+1)
            if dfs(u,v,vis):
                return [u,v]
            adj[u].append(v)
            adj[v].append(u)