class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res=[]
        def backtrack(i,parts):
            if len(parts)==4:
                if i==len(s):
                    res.append(".".join(parts))
                return
            for j in range(i,min(i+3,len(s))):
                part=s[i:j+1]
                if len(part)>1 and part[0]=='0':
                    break
                if int(part)>255:
                    break
                parts.append(part)
                backtrack(j+1,parts)
                parts.pop()
        backtrack(0,[])
        return res

        