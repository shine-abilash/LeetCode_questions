class Solution:
    def containsCycle(self, grid: list[list[str]]) -> bool:
        n=len(grid)
        m=len(grid[0])
        vis=[[False]*m for i in range(n)]
        def dfs(x,y,tx,ty):
            vis[x][y]=True
            moves=[(1,0),(-1,0),(0,1),(0,-1)]
            for dx,dy in moves:
                nx=dx+x
                ny=dy+y
                if nx<0 or ny<0 or nx>=n or ny>=m:
                    continue
                if grid[x][y]!=grid[nx][ny]:
                    continue
                if (nx,ny)==(tx,ty):
                    continue
                if vis[nx][ny]:
                    return True
                if dfs(nx,ny,x,y):
                    return True
            return False

        for i in range(n):
            for j in range(m):
                if not vis[i][j]:
                    if dfs(i,j,-1,-1):
                        return True
        return False