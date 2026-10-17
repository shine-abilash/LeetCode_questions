class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        n=len(grid)
        m=len(grid[0])
        start=None
        all_keys=set()
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='@':
                    start=(i,j)
                if grid[i][j].islower():
                    all_keys.add(grid[i][j])
        target=len(all_keys)
        if target==0:
            return 0
        r,c=start
        moves=[(1,0),(-1,0),(0,1),(0,-1)]
        queue=[(r,c,frozenset(),0)]
        vis={(r,c,frozenset())}
        while queue:
            r,c,keys,dist=queue.pop(0)
            if len(keys)==target:
                return dist
            for dx,dy in moves:
                nx=r+dx
                ny=c+dy
                if nx<0 or ny<0 or nx>=n or ny>=m:
                    continue
                cell=grid[nx][ny]
                if cell=='#':
                    continue
                if cell.isupper() and cell.lower() not in keys:
                    continue
                new_keys=keys
                if cell.islower():
                    new_keys=frozenset([cell])|keys
                state=(nx,ny,new_keys)
                if state not in vis:
                    vis.add(state)
                    queue.append((nx,ny,new_keys,dist+1))
        return -1