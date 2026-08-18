class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        emt=0
        def backtrack(x,y,count):
            if x<0 or y<0 or x>=row or y>=col or grid[x][y]==-1 or sol[x][y]==1:
                return 0
            if grid[x][y]==2:
                if emt==count:
                    return 1
                return 0
            sol[x][y]=1
            path=0
            path+=backtrack(x+1,y,count+1)
            path+=backtrack(x,y+1,count+1)
            path+=backtrack(x-1,y,count+1)
            path+=backtrack(x,y-1,count+1)
            sol[x][y]=0
            return path

        sol=[[0]*col for i in range(row)]
        for i in range(row):
            for j in range(col):
                if grid[i][j]!=-1:
                    emt=emt+1
                if grid[i][j]==1:
                    start_i,start_j=i,j
        return backtrack(start_i,start_j,1)