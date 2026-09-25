class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        old_color=image[sr][sc]
        if old_color==color:
            return image
        queue=[(sr,sc)]
        image[sr][sc]=color
        moves=[(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            i,j=queue.pop(0)
            for dx,dy in moves:
                nx=i+dx
                ny=j+dy
                if 0<=nx<len(image) and 0<=ny<len(image[0]) and image[nx][ny]==old_color:
                    image[nx][ny]=color
                    queue.append((nx,ny))
        return image
