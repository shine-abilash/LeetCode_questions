class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        n=len(grid)
        queue=[]
        found=False
        def dfs(x,y):
            if x<0 or y<0 or x>=n or y>=n:
                return
            if grid[x][y]!=1:
                return 
            grid[x][y]=2
            queue.append((x,y))
            dfs(x+1,y)
            dfs(x,y+1)
            dfs(x-1,y)
            dfs(x,y-1)

        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    dfs(i,j)
                    found=True
                    break
            if found:
                break

        steps=0
        moves=[(1,0),(-1,0),(0,1),(0,-1)]

        while queue:
            for i in range(len(queue)):
                x,y=queue.pop(0)
                for dx,dy in moves:
                    nx=x+dx
                    ny=y+dy
                    if nx<0 or ny<0 or nx>=n or ny>=n:
                        continue
                    if grid[nx][ny]==1:
                        return steps
                    if grid[nx][ny]==0:
                        grid[nx][ny]=2
                        queue.append((nx,ny))
            steps+=1