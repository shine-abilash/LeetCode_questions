class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        n=len(heights)
        m=len(heights[0])
        pacific=[[False]*m for i in range(n)]
        atlantic=[[False]*m for i in range(n)]
        r=[]
        def dfs(x,y,vis):
            vis[x][y]=True
            moves=[(1,0),(-1,0),(0,1),(0,-1)]
            for dx,dy in moves:
                nx=x+dx
                ny=y+dy
                if nx<0 or ny<0 or nx>=n or ny>=m:
                    continue
                if vis[nx][ny]:
                    continue
                if heights[nx][ny]<heights[x][y]:
                    continue
                dfs(nx,ny,vis)

        for i in range(m):
            dfs(0,i,pacific)
        for j in range(n):
            dfs(j,0,pacific)
        for i in range(m):
            dfs(n-1,i,atlantic)
        for j in range(n):
            dfs(j,m-1,atlantic)
        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    r.append([i,j])
        return r