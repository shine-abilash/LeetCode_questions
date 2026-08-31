class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])
        sol=[[0]*col for i in range(row)]
        def find(x,y,ind):
            if ind==len(word):
                return True
            if x<0 or y<0 or x>=row or y>=col:
                return False
            if board[x][y]!=word[ind] or sol[x][y]==1:
                return False
            sol[x][y]=1
            if find(x+1,y,ind+1):
                return True
            if find(x,y+1,ind+1):
                return True
            if find(x-1,y,ind+1):
                return True
            if find(x,y-1,ind+1):
                return True
            sol[x][y]=0
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if find(i,j,0):
                        return True
        return False