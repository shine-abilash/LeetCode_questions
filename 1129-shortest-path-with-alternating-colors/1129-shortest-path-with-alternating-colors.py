class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        red=[[] for i in range(n)]
        blue=[[] for j in range(n)]
        for u,v in redEdges:
            red[u].append(v)
        for u,v in blueEdges:
            blue[u].append(v)
        queue=[(0,0),(0,1)]
        vis={(0,0),(0,1)}
        dist=[-1]*n
        dist[0]=0
        d=0
        while queue:
            for i in range(len(queue)):
                node,color=queue.pop(0)
                if color==0:
                    next_edge=blue
                    next_color=1
                else:
                    next_edge=red
                    next_color=0
                for v in next_edge[node]:
                    state=(v,next_color)
                    if state not in vis:
                        vis.add(state)
                        queue.append(state)
                        if dist[v]==-1:
                            dist[v]=d+1
            d+=1
        return dist