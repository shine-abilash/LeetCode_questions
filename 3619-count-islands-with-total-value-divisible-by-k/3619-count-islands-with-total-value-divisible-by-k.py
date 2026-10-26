class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n=len(grid)
        m=len(grid[0])
        vis=[[False]*m for i in range(n)]
        '''def dfs(x,y):
            if x<0 or y<0 or x>=n or y>=m:
                return 0
            if grid[x][y]==0 or vis[x][y]:
                return 0
            vis[x][y]=True
            c=grid[x][y]
            c+=dfs(x+1,y)
            c+=dfs(x,y+1)
            c+=dfs(x-1,y)
            c+=dfs(x,y-1)
            return c'''

        def bfs(x,y):
            queue=[(x,y)]
            vis[x][y]=True
            c=0
            moves=[(1,0),(-1,0),(0,1),(0,-1)]
            while queue:
                for i in range(len(queue)):
                    x,y=queue.pop(0)
                    c+=grid[x][y]
                    for dx,dy in moves:
                        nx=x+dx
                        ny=y+dy
                        if nx<0 or ny<0 or nx>=n or ny>=m:
                            continue
                        if grid[nx][ny]==0 or vis[nx][ny]:
                            continue
                        vis[nx][ny]=True
                        queue.append((nx,ny))
            return c

        count=0

        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0 and vis[i][j]==False:
                    s=bfs(i,j)
                    if s%k==0:
                        count+=1
        return count