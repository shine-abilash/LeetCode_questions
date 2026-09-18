class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj=[[] for i in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        vis=[False]*n
        queue=[source]
        vis[source]=True
        found=False
        while queue:
            node=queue.pop(0)
            if node==destination:
                found=True
                break
            for v in adj[node]:
                if not vis[v]:
                    vis[v]=True
                    queue.append(v)
        if found:
            return True
        else:
            return False