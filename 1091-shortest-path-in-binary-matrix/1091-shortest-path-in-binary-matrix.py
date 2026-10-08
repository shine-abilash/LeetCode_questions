class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        vis=[[False]*m for i in range(n)]
        queue=[(0,0)]
        vis[0][0]=True
        d=1
        if grid[0][0]==1 or grid[n-1][m-1]==1:
            return -1
        moves=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        while queue:
            for i in range(len(queue)):
                x,y=queue.pop(0)
                if x==n-1 and y==m-1:
                    return d
                for dx,dy in moves:
                    nx=x+dx
                    ny=y+dy
                    if 0<=nx<n and 0<=ny<m and grid[nx][ny]!=1:
                        if not vis[nx][ny]:
                            vis[nx][ny]=True
                            queue.append((nx,ny))
            d+=1
        else:
            return -1
