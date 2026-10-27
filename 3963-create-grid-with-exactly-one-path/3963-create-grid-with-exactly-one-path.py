class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        arr = [['#'] * n for i in range(m)]

        def dfs(x, y):
            if x < 0 or y < 0 or x >= m or y >= n:
                return False

            if arr[x][y] != '#':
                return False

            arr[x][y] = '.'

            if x == m - 1 and y == n - 1:
                return True

            if dfs(x + 1, y):
                return True

            if dfs(x, y + 1):
                return True

            arr[x][y] = '#'
            return False

        dfs(0, 0)

        return [''.join(row) for row in arr]