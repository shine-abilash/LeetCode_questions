class Solution:
    def totalNQueens(self, n: int) -> int:
        count=0
        cols=set()
        diag1=set()
        diag2=set()
        def dfs(r):
            nonlocal count
            if r==n:
                count+=1
                return
            for col in range(n):
                if col in cols:
                    continue
                if r-col in diag1:
                    continue
                if r+col in diag2:
                    continue
                cols.add(col)
                diag1.add(r-col)
                diag2.add(r+col)
                dfs(r+1)
                cols.remove(col)
                diag1.remove(r-col)
                diag2.remove(r+col)

        dfs(0)
        return count