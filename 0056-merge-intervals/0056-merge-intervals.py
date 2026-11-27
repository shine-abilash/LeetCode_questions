class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        ch=intervals[0]
        res=[]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=ch[1]:
                ch[1]=max(intervals[i][1],ch[1])
            else:
                res.append(ch)
                ch=intervals[i]
        res.append(ch)
        return res