class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        vis=[False]*(len(rooms))
        queue=[0]
        vis[0]=True
        while queue:
            u=queue.pop(0)
            for v in rooms[u]:
                if not vis[v]:
                    vis[v]=True
                    queue.append(v)
        return all(vis)