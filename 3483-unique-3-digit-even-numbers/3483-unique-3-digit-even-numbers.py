class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        res=set()
        used=[False]*len(digits)
        def dfs(path):
            if len(path)==3:
                if path[2]%2==0:
                    num=path[0]*100+path[1]*10+path[2]*1
                    res.add(num)
                return
            for i in range(len(digits)):
                if used[i]:
                    continue
                if len(path)==0 and digits[i]==0:
                    continue
                used[i]=True
                path.append(digits[i])
                dfs(path)
                path.pop()
                used[i]=False

        dfs([])
        return (len(res))