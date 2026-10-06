import heapq
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph=[[] for i in range(n+1)]
        for u,v,w in times:
            graph[u].append((v,w))
        INF=float('inf')
        dist=[INF]*(n+1)
        dist[k]=0
        hq=[(0,k)]
        while hq:
            distance,node=heapq.heappop(hq)
            if distance>dist[node]:
                continue
            for v,w in graph[node]:
                new_dist=distance+w
                if new_dist<dist[v]:
                    dist[v]=new_dist
                    heapq.heappush(hq,(new_dist,v))
        ans=max(dist[1:])
        if ans==INF:
            return -1
        return ans