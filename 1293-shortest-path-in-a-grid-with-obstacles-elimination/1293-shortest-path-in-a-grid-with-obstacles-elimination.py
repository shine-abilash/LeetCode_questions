class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        n=len(grid)
        m=len(grid[0])
        queue=[(0,0,k)]
        vis={(0,0,k)}
        moves=[(1,0),(-1,0),(0,1),(0,-1)]
        d=0
        while queue:
            for i in range(len(queue)):
                x,y,remain=queue.pop(0)
                if x==n-1 and y==m-1:
                    return d
                for dx,dy in moves:
                    nx=x+dx
                    ny=y+dy
                    if nx<0 or ny<0 or nx>=n or ny>=m:
                        continue
                    new_remain=remain-grid[nx][ny]
                    if new_remain<0:
                        continue
                    state=(nx,ny,new_remain)
                    if state not in vis:
                        vis.add(state)
                        queue.append(state)
            d=d+1
        else:
            return -1
