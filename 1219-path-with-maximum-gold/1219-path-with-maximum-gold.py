from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = [[False] * col for _ in range(row)]

        def backtrack(x, y):
            if x < 0 or y < 0 or x >= row or y >= col or grid[x][y] == 0 or visited[x][y]:
                return 0
            
            gold = grid[x][y]
            visited[x][y] = True
            
            up = backtrack(x - 1, y)
            down = backtrack(x + 1, y)
            right = backtrack(x, y + 1)
            left = backtrack(x, y - 1)
            
            visited[x][y] = False  
            
            return gold + max(up, down, right, left)

        max_gold = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, backtrack(i, j))
        
        return max_gold