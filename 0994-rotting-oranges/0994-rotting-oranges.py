class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        queue=[]
        fresh=0
        d=0
        n=len(grid)
        m=len(grid[0])
        moves=[(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        while queue  and fresh:
            for i in range(len(queue)):
                x,y=queue.pop(0)
                for dx,dy in moves:
                    nx=x+dx
                    ny=y+dy
                    if 0<=nx<n and 0<=ny<m:
                        if grid[nx][ny]==1:
                            grid[nx][ny]=2
                            queue.append((nx,ny))
                            fresh-=1
            d=d+1
        if fresh>0:
            return -1
        else:
            return d