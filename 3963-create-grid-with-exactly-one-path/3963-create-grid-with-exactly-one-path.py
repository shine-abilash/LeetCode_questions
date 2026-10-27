class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        arr=[[0]*n for i in range(m)]
        for i in range(m):
            arr[i][0]='.'
        for i in range(n):
            arr[m-1][i]='.'
        for i in range(m):
            for j in range(n):
                if arr[i][j]!='.':
                    arr[i][j]='#'
        s=str(arr)
        r=[''.join(i) for i in arr]
        return r