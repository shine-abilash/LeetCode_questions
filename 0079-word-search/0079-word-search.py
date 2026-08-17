class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])

        def dfs(x,y,i):
            if i==len(word):
                return True
            if x<0 or y<0 or x>=row or y>=col or board[x][y]!=word[i] or sol[x][y]==1:
                return False
            sol[x][y]=1
            if dfs(x+1,y,i+1):
                return True
            if dfs(x,y+1,i+1):
                return True
            if dfs(x-1,y,i+1):
                return True
            if dfs(x,y-1,i+1):
                return True
            sol[x][y]=0
            return False

        sol=[[0]*col for i in range(row)]
        for i in range(row):
            for j in range(col):
                if dfs(i,j,0):
                    return True
        else:
            return False