import heapq
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        queue=[(0,0,0)]
        row=len(heights)
        col=len(heights[0])
        INF=float('inf')
        best=[[INF]*col for i in range(row)]
        best[0][0]=0
        moves=[(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            e,i,j=heapq.heappop(queue)
            if i==row-1 and j==col-1:
                return e
            if e>best[i][j]:
                continue
            for dx,dy in moves:
                nx=i+dx
                ny=j+dy
                if 0<=nx<row and 0<=ny<col:
                    dist=abs(heights[nx][ny]-heights[i][j])
                    new_dist=max(dist,e)
                    if new_dist<best[nx][ny]:
                        best[nx][ny]=new_dist
                        heapq.heappush(queue,(new_dist,nx,ny))
        return 0