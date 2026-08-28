class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(curr,opn,clo):
            if len(curr)==n*2:
                res.append(curr)
                return
            if opn<n:
                dfs(curr+'(',opn+1,clo)
            if clo<opn:
                dfs(curr+')',opn,clo+1)

        dfs('',0,0)
        return res

        