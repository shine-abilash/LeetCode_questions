class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        c=0
        vis=[False]*n
        def dfs(city):
            vis[city]=True
            for j in range(n):
                if isConnected[city][j]==1 and vis[j]==False:
                    dfs(j)

        for i in range(n):
            if vis[i]==False:
                c=c+1
                dfs(i)
        return c