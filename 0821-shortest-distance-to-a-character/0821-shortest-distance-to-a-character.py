class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        r=[]
        for i in range(len(s)):
            if s[i]==c:
                r.append(i)
        f=[]
        for i in range(len(s)):
            a=[]
            for j in range(len(r)):
                g=abs(r[j]-i)
                a.append(g)
            f.append(min(a))
        return f