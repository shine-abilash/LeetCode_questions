class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        find=[False]*n
        adj=[[] for i in range(n)]
        for u,v in edges:
            adj[u].append(v)
        for u,v in edges:
            find[v]=True
        r=[]
        for i in range(n):
            if not find[i]:
                r.append(i)
        return r
        

        '''def dfs(node):
            for v in adj[node]:
                find[v]=True
                dfs(v)

        for i in range(n):
            if not find[i]:
                dfs(i)
        r=[]
        for i in range(len(find)):
            if find[i]:
                continue
            else:
                r.append(i)
        return r'''