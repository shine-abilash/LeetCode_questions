class Solution:
    def findOrder(self, n: int, prerequisites: list[list[int]]) -> list[int]:
        adj=[[] for i in range(n)]
        for u,v in prerequisites:
            adj[v].append(u)
        col=[0]*n
        order=[]
        def dfs(node):
            col[node]=1
            for v in adj[node]:
                if col[v]==1:
                    return True
                if col[v]==0:
                    if dfs(v):
                        return True
            col[node]=2
            order.append(node)
            return False

        for i in range(n):
            if col[i]==0:
                if dfs(i):
                    return []
        return order[::-1]