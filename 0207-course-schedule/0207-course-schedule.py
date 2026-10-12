class Solution:
    def canFinish(self, n: int, prerequisites: list[list[int]]) -> bool:
        adj=[[] for i in range(n)]
        for u,v in prerequisites:
            adj[v].append(u)
        col=[0]*n
        def dfs(node):
            col[node]=1
            for v in adj[node]:
                if col[v]==1:
                    return True
                if col[v]==0:
                    if dfs(v):
                        return True
            col[node]=2
            return False

        for i in range(n):
            if col[i]==0:
                if dfs(i):
                    return False
        return True