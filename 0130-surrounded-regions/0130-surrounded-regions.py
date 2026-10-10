class Solution:
    def solve(self, board: list[list[str]]) -> None:
        n=len(board)
        m=len(board[0])
        def dfs(x,y):
            if x<0 or y<0 or x>=n or y>=m:
                return
            if board[x][y]!='O':
                return
            board[x][y]='#'
            dfs(x+1,y)
            dfs(x,y+1)
            dfs(x-1,y)
            dfs(x,y-1)
        for i in range(n):
            dfs(i,0)
            dfs(i,m-1)
        for i in range(m):
            dfs(0,i)
            dfs(n-1,i)

        for i in range(n):
            for j in range(m):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='#':
                    board[i][j]='O'
        